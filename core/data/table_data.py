"""
Dados específicos para o componente Table
"""

# Dados básicos para Table
TABLE_BASIC_DATA = {
    'headers': ['Nome', 'E-mail', 'Cargo', 'Status'],
    'data': [
        ['Ana Silva', 'ana@email.com', 'Desenvolvedora', 'Ativo'],
        ['Carlos Santos', 'carlos@email.com', 'Designer', 'Ativo'],
        ['Maria Oliveira', 'maria@email.com', 'Gerente', 'Inativo'],
        ['João Pereira', 'joao@email.com', 'Analista', 'Ativo'],
    ]
}

# Dados para tabela responsiva
TABLE_RESPONSIVE_DATA = {
    'headers': ['ID', 'Nome', 'E-mail', 'Cargo', 'Departamento', 'Data Admissão', 'Status', 'Telefone'],
    'data': [
        ['001', 'Ana Silva', 'ana@email.com', 'Desenvolvedora', 'Tecnologia', '15/03/2023', 'Ativo', '(11) 99999-0001'],
        ['002', 'Carlos Santos', 'carlos@email.com', 'Designer', 'Marketing', '22/07/2022', 'Ativo', '(11) 99999-0002'],
        ['003', 'Maria Oliveira', 'maria@email.com', 'Gerente', 'Vendas', '10/01/2021', 'Inativo', '(11) 99999-0003'],
        ['004', 'João Pereira', 'joao@email.com', 'Analista', 'Financeiro', '05/11/2023', 'Ativo', '(11) 99999-0004'],
        ['005', 'Lucia Costa', 'lucia@email.com', 'Desenvolvedora', 'Tecnologia', '18/09/2022', 'Ativo', '(11) 99999-0005'],
    ]
}

TABLE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>headers</code>', 'list', '-', 'Lista de cabeçalhos'],
        ['<code>rows</code>', 'list', '-', 'Lista de linhas de dados'],
        ['<code>hover</code>', 'boolean', 'false', 'Habilita hover nas linhas'],
        ['<code>responsive</code>', 'boolean', 'false', 'Tabela responsiva'],
        ['<code>striped</code>', 'boolean', 'false', 'Linhas alternadas'],
        ['<code>bordered</code>', 'boolean', 'false', 'Bordas nas células'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

TABLE_DATA = {
    'basic_data': TABLE_BASIC_DATA,
    'responsive_data': TABLE_RESPONSIVE_DATA,
    'params': TABLE_PARAMS
}
