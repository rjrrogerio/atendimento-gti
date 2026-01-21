const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const {
    normalize_name,
    name_split,
    get_uo,
    create_password,
    get_data_script_add,
    unidades
} = require('./utils/script_novo_usuario');

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Routes
app.get('/', (req, res) => {
    res.redirect('/criausuario');
});

app.get('/criausuario', (req, res) => {
    res.render('create_user', {
        query_unidade: unidades,
        dados_script: [],
        messages: []
    });
});

app.post('/criausuario', (req, res) => {
    let dados_script = [];
    let dados_funcionario = [];
    let dados_aliases = [];
    let dados_grupos = [];
    let messages = [];

    const countField = parseInt(req.body.countField) || 0;

    // Helper to get field value safely handling array/object structure from body-parser
    const getField = (fieldName, index) => {
        if (req.body[fieldName] && req.body[fieldName][index]) {
            return req.body[fieldName][index];
        }
        return '';
    };

    // In Django request.POST.get('field_nome[{}]'.format(i)) suggests the name in HTML is literally "field_nome[0]".
    // Body-parser with extended:true (qs) parses "field_nome[0]" as:
    // req.body.field_nome is an array (if indices are 0, 1...) or object {'0': 'val'}.
    // We can access it via req.body.field_nome[index].

    for (let i = 0; i < countField; i++) {
        try {
            const rawName = getField('field_nome', i);
            const nome_completo = normalize_name(rawName);
            const { primeiro_nome, sobrenome } = name_split(nome_completo);

            const uoId = getField('field_uo', i);
            const objeto_unidade = get_uo(uoId);

            const data_nao_normalizada = getField('field_data_contrato', i);
            const nome_logon = getField('field_email', i);
            const email = nome_logon + "@sescsp.org.br";

            const numero_uo = objeto_unidade.numeroUo;
            let descricao = objeto_unidade.nomeUo;

            let grupos = objeto_unidade.grupoUo; // String or handle split inside utility if needed, utility handles it.

            const tipo = getField('field_tipo', i);
            if (tipo !== 'funcionario') {
                descricao = descricao + " - " + tipo;
            }

            let grupos_gerais = [];
            let sede_ou_unidade = '';

            if (objeto_unidade.local === 'sede') {
                grupos_gerais = ["Grupo Geral Sede SescSP"];
                sede_ou_unidade = 'SEDE';
            } else if (objeto_unidade.local === 'capital') {
                grupos_gerais = ["Grupo Geral Unidades SescSP", "Grupo Geral Unidades da Capital SescSP"];
                sede_ou_unidade = 'UNIDADES';
            } else {
                grupos_gerais = ["Grupo Geral Unidades SescSP", "Grupo Geral Unidades do Interior SescSP"];
                sede_ou_unidade = 'UNIDADES';
            }

            const nome_uo_ad = objeto_unidade.nomeUOnoAD;
            const nome_uo = objeto_unidade.nomeUo;
            const escritorio = "SESC " + objeto_unidade.nomeUo;
            const cidade_uo = objeto_unidade.cidadeUo;
            const estado_uo = objeto_unidade.estado;
            const licenca = getField('field_licenca', i);
            const data_contrato = data_nao_normalizada;
            const senha = create_password(nome_completo, uoId);

            const result = get_data_script_add(
                dados_script, dados_funcionario, dados_aliases, dados_grupos, primeiro_nome,
                sobrenome, nome_completo, nome_logon, email,
                numero_uo, nome_uo, descricao, grupos, grupos_gerais,
                tipo, escritorio, cidade_uo, estado_uo, sede_ou_unidade,
                licenca, nome_uo_ad, data_contrato, senha
            );

            // Result updates the arrays in place (passed by reference) in Python,
            // but in JS arrays passed as args are references, so push works.
            // My JS function returns object with them too.
            // But since I passed empty arrays and pushed to them in function, they should be updated.
            // Let's rely on the return value to be safe/cleaner if I reassigned them, but I pushed.
            // Actually in my JS implementation I pushed to them.

        } catch (err) {
            console.error(`Error processing row ${i}:`, err);
            messages.push({ type: 'error', text: `Erro na linha ${i+1}: ${err.message}` });
        }
    }

    // Mock save_log and save_group
    // console.log("Saving log and groups...");

    dados_funcionario.forEach(d => messages.push({ type: 'success', text: d }));
    dados_aliases.forEach(d => messages.push({ type: 'info', text: d }));

    res.render('create_user', {
        query_unidade: unidades,
        dados_script: dados_script,
        messages: messages
    });
});

// Start server
app.listen(port, () => {
    console.log(`App running on http://localhost:${port}`);
});
