const unidecode = require('unidecode');
const fs = require('fs');
const path = require('path');

// Load unidades
const unidadesPath = path.join(__dirname, '../data/unidades.json');
let unidades = [];
try {
    const data = fs.readFileSync(unidadesPath, 'utf8');
    unidades = JSON.parse(data);
} catch (err) {
    console.error("Error loading unidades:", err);
}

function create_password(fullname, unidade) {
    const iniciais_do_nome = fullname.split(" ").map(letra => letra[0]).join("");
    const randomNum = Math.floor(Math.random() * (999 - 100 + 1)) + 100;

    // Python's title() on "NS" -> "Ns".
    const initialsTitle = iniciais_do_nome.charAt(0).toUpperCase() + iniciais_do_nome.slice(1).toLowerCase();
    const senha = `${randomNum}_${initialsTitle}#${unidade}`;
    return senha;
}

function name_split(fullname) {
    let primeiro_nome, sobrenome;
    try {
        const parts = fullname.split(" ");
        primeiro_nome = parts[0];
        sobrenome = parts.slice(1).join(" ");
        if (!sobrenome) sobrenome = "";
    } catch (e) {
        primeiro_nome = fullname;
        sobrenome = "";
    }
    return { primeiro_nome, sobrenome };
}

function normalize_name(fullname) {
    const nome_sem_espaco = fullname.trimStart();
    const nome_sem_acento = unidecode(nome_sem_espaco);
    // Title case in JS
    const nome_normalizado = nome_sem_acento.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    return nome_normalizado;
}

function get_uo(numeroUo) {
    const unidade = unidades.find(u => u.numeroUo == numeroUo);
    if (!unidade) {
        throw new Error(`Unidade with number ${numeroUo} not found`);
    }
    return unidade;
}

function normalize_date(data) {
    // Input format YYYY-MM-DD (from HTML date input), Output DD/MM/YYYY
    if (!data) return null;
    try {
        const [year, month, day] = data.split('-');
        if (!year || !month || !day) return null;
        return `${day}/${month}/${year}`;
    } catch (e) {
        return null;
    }
}

function get_license(licenca, tipo) {
    let tipo_de_licenca = '';
    if (licenca === 'lica1') {
        tipo_de_licenca = 'LIC-A1-';
    } else {
        tipo_de_licenca = 'LIC-A3-';
    }

    if (licenca === 'lica1' && tipo === 'funcionario') {
        tipo_de_licenca += 'SESCSP-SG';
    } else if (tipo === 'funcionario') {
        tipo_de_licenca += 'SESCSP_SG';
    } else if (tipo === 'estagiario') {
        tipo_de_licenca += 'ESTAGIARIOS_SG';
    } else if (tipo === 'temporario' || tipo === 'terceiro') {
        tipo_de_licenca += 'TEMPORARIOS_SG';
    } else {
        tipo_de_licenca += 'APRENDIZES_SG';
    }
    return tipo_de_licenca;
}

function get_data_script_add(dados_script, dados_funcionario, dados_aliases, dados_grupos, primeiro_nome,
    sobrenome, nome_completo, nome_logon, email, numero_uo,
    nome_uo, descricao, grupos, grupos_gerais, tipo, escritorio,
    cidade_uo, estado_uo, sede_ou_unidade, licenca,
    nome_uo_ad, data_contrato, senha) {

    const server_name = '-Server "srv-ad-prd01.sescsp.local"';

    dados_funcionario.push(`Usuário: ${nome_logon} - Senha: ${senha} - UO: ${nome_uo}`);
    dados_aliases.push(`grep -q "^${nome_logon}:" /etc/aliases || { echo "${nome_logon}: ${nome_logon}@sede.sescsp.org.br" >> /etc/aliases && newaliases; }`);

    const tipo_de_licenca = get_license(licenca, tipo);
    const data_contrato_normalizada = normalize_date(data_contrato);

    if (escritorio === "SESC Mogi das Cruzes") {
        nome_uo_ad = "72-Mogi das Cruzes\\ ";
    }

    if (tipo === "Terceiro") {
        escritorio = escritorio + " - Terceiro";
    }

    const cmd1 = `if (!(Get-aduser -filter {samaccountname -eq "${nome_logon}"})) {New-ADUser -Name "${nome_completo}" ${server_name} -GivenName "${primeiro_nome}" -Surname "${sobrenome}" -SamAccountName "${nome_logon}" -DisplayName "${nome_completo}" -Company "SESCSP" -UserPrincipalName "${nome_logon}@sescsp.org.br" -EmailAddress "${email}" -Description "${descricao}" -Office "${escritorio}" -Department "${nome_uo}" -City "${cidade_uo}" -State "${estado_uo}" -AccountPassword (ConvertTo-SecureString -AsPlainText “${senha}” -Force) -ChangePasswordAtLogon $True -Path "OU=Usuarios,OU=${nome_uo_ad},OU=${sede_ou_unidade},DC=sescsp,DC=local" -Enabled $True;`;

    dados_script.push(cmd1);

    dados_script.push(`Set-ADUser ${server_name} ${nome_logon} -add @{ProxyAddresses="smtp:${nome_logon}@sede.sescsp.org.br,SMTP:${nome_logon}@sescsp.org.br" -split ","};`);

    if (grupos) {
        let gruposList = [];
        if (Array.isArray(grupos)) {
             gruposList = grupos;
        } else if (typeof grupos === 'string') {
             gruposList = grupos.split(',').map(s => s.trim()).filter(s => s);
        }

        gruposList.forEach(grupo => {
            dados_script.push(`Add-ADGroupMember ${server_name} -Identity "${grupo}" -Members ${nome_logon};`);
        });
    }

    grupos_gerais.forEach(grupo => {
        dados_grupos.push(`Add-DistributionGroupMember -Identity "${grupo}" -Member ${nome_logon};`);
    });

    dados_script.push(`Add-ADGroupMember -Identity "${tipo_de_licenca}" -Members ${nome_logon} ${server_name};`);

    if (tipo !== 'funcionario' && data_contrato_normalizada) {
        dados_script.push(`Get-ADUser -Identity ${nome_logon} ${server_name} | Set-AdUser -AccountExpirationDate "${data_contrato_normalizada}" ${server_name};`);
    }

    dados_script.push(`} else { write-host 'Usuário ${nome_logon} já existe'};`);

    return { dados_script, dados_funcionario, dados_aliases, dados_grupos };
}

module.exports = {
    create_password,
    name_split,
    normalize_name,
    get_uo,
    normalize_date,
    get_license,
    get_data_script_add,
    unidades
};
