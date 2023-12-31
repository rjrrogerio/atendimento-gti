import unittest
import re
from create_user_app.utils.script_novo_usuario import name_split
from create_user_app.utils.script_novo_usuario import normalize_name
from create_user_app.utils.script_novo_usuario import normalize_date
from create_user_app.utils.script_novo_usuario import get_license
from create_user_app.utils.script_novo_usuario import create_password
from create_user_app.utils.script_novo_usuario import get_data_script

class TestCreateUserAD(unittest.TestCase):

    def test_create_password_pattern(self):
        test_cases = [
            ("Rogerio Vieira da Silva Junior", "27"),
            ("Ana Santos", "53"),
            ("Paulo Martins", "98"),
            ("Maria Souza", "34"),
            ("José Lima", "72"),
            ("Camila Ferreira", "11"),
            ("Rafael Silva", "56"),
            ("Fernanda Oliveira", "23"),
            ("Bruno Rodrigues", "89"),
            ("Amanda Costa", "67")
        ]
        
        for fullname, unidade in test_cases:
            with self.subTest(fullname=fullname, unidade=unidade):
                generated_password = create_password(fullname, unidade)
                self.assertTrue(self.is_valid_password(generated_password))

    def is_valid_password(self, password):
        valid_pattern = r"^\d{3}_[A-Z][a-z]*#[0-9]{2}$"
        return re.match(valid_pattern, password) is not None
    
    def test_name_split(self):
        test_cases = [
            ("Rogerio Vieira da Silva Junior", ("Rogerio", "Vieira da Silva Junior")),
            ("Ana Santos", ("Ana", "Santos")),
            ("Paulo Martins", ("Paulo", "Martins")),
            ("Maria Souza", ("Maria", "Souza")),
            ("José Lima", ("José", "Lima")),
            ("Camila Ferreira", ("Camila", "Ferreira")),
            ("Rafael Silva", ("Rafael", "Silva")),
            ("Rogerio", ("Rogerio", "")),
            ("Fernanda Oliveira", ("Fernanda", "Oliveira")),
            ("Bruno Rodrigues", ("Bruno", "Rodrigues")),
            ("Amanda Costa", ("Amanda", "Costa")),
        ]
        
        for fullname, expected_names in test_cases:
            with self.subTest(fullname=fullname):
                first_name, last_name = name_split(fullname)
                self.assertEqual(first_name, expected_names[0])
                self.assertEqual(last_name, expected_names[1])

    def test_normalize_name(self):
        test_cases = [
            ("José da Silva", "Jose Da Silva"),
            ("john DOE", "John Doe"),
            ("Maria Souza", "Maria Souza"),
            ("Antônio OLIVEIRA", "Antonio Oliveira"),
            ("AnA Santos", "Ana Santos"),
            ("Fernanda Lima", "Fernanda Lima"),
            ("Pedro Ferreira", "Pedro Ferreira"),
            ("Camila MArTINs", "Camila Martins"),
            ("Rafael Rodrigues", "Rafael Rodrigues"),
            ("ISABELA Costa", "Isabela Costa"),
        ]
        
        for input_name, expected_normalized in test_cases:
            with self.subTest(input_name=input_name):
                normalized_name = normalize_name(input_name)
                self.assertEqual(normalized_name, expected_normalized)

    def test_normalize_date(self):
        test_cases = [
            ("2023-03-23", "23/03/2023"),
            ("2022-12-31", "31/12/2022"),
            ("invalid-date", None),
            ("2021-01-15", "15/01/2021"),
            ("2022-07-10", "10/07/2022"),
            ("2023-09-05", "05/09/2023"),
            ("2020-04-02", "02/04/2020"),
            ("2024-11-20", "20/11/2024"),
            ("2025-08-18", "18/08/2025"),
            ("2026-06-27", "27/06/2026"),
            ("2027-02-09", "09/02/2027"),
        ]
        
        for input_date, expected_normalized in test_cases:
            with self.subTest(input_date=input_date):
                normalized_date = normalize_date(input_date)
                self.assertEqual(normalized_date, expected_normalized)

    def test_get_license(self):
        test_cases = [
            ('lica1', 'funcionario', 'LIC-A1-SESCSP-SG'),
            ('lica2', 'estagiario', 'LIC-A3-ESTAGIARIOS_SG'),
            ('lica3', 'temporario', 'LIC-A3-TEMPORARIOS_SG'),
            ('lica4', 'outro', 'LIC-A3-APRENDIZES_SG'),
        ]
        
        for licenca, tipo, expected_license in test_cases:
            with self.subTest(licenca=licenca, tipo=tipo):
                license_string = get_license(licenca, tipo)
                self.assertEqual(license_string, expected_license)

    def test_get_data_script(self):
        dados_script = []
        dados_funcionario = []
        dados_aliases = []
        primeiro_nome = "Rogério"
        sobrenome = "Vieira da Silva Júnior"
        nome_completo = "Rogério Vieira da Silva Júnior"
        nome_logon = "rogerio.junior"
        email = "rogerio.junior@sescsp.org.br"
        numero_uo = "15"
        nome_uo = "GTI"
        descricao = "Descrição do usuário"
        grupos = ["Grupo1", "Grupo2"]
        grupos_gerais = ["GrupoGeral1", "GrupoGeral2"]
        tipo = "funcionario"
        escritorio = "Escritório Sesc"
        cidade_uo = "São Paulo"
        estado_uo = "SP"
        sede_ou_unidade = "Sede"
        licenca = "lica3"
        nome_uo_ad = "nome_ad_gti"
        data_contrato = "2023-03-23"
        senha = "123_Rvdsj#15"

        dados_script, dados_funcionario, dados_aliases = get_data_script(
            dados_script, dados_funcionario, dados_aliases, primeiro_nome, sobrenome,
            nome_completo, nome_logon, email, numero_uo, nome_uo, descricao, grupos,
            grupos_gerais, tipo, escritorio, cidade_uo, estado_uo, sede_ou_unidade,
            licenca, nome_uo_ad, data_contrato, senha
        )

        assert len(dados_script) == 6
        assert len(dados_funcionario) == 1
        assert len(dados_aliases) == 1
        assert nome_logon in dados_script[0]
        assert nome_logon in dados_script[1]
        assert nome_logon in dados_script[2]
        assert nome_logon in dados_funcionario[0]
        assert nome_logon in dados_aliases[0]

if __name__ == '__main__':
    unittest.main()