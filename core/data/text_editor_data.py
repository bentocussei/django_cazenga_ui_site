# Dados do componente Text Editor

# Editor de texto básico
text_editor_basic = {
    'toolbar': ['bold', 'italic', 'underline', 'strike', '|', 'heading1', 'heading2', 'heading3', '|', 'bulletList', 'orderedList', '|', 'link', 'blockquote'],
    'placeholder': 'Digite seu texto aqui...',
    'content': '<p>Este é um exemplo de conteúdo no editor. Você pode <strong>formatar texto</strong>, criar <em>ênfase</em> e muito mais.</p>',
    'height': 'h-64',
    'editable': True
}

# Editor de texto completo (como Word/Google Docs)
text_editor_complete = {
    'toolbar': [
        'undo', 'redo', '|',
        'bold', 'italic', 'underline', 'strike', 'code', '|',
        'heading1', 'heading2', 'heading3', 'heading4', 'heading5', 'heading6', '|',
        'paragraph', 'bulletList', 'orderedList', 'taskList', '|',
        'textAlign:left', 'textAlign:center', 'textAlign:right', 'textAlign:justify', '|',
        'indent', 'outdent', '|',
        'textColor', 'backgroundColor', '|',
        'link', 'unlink', 'image', 'table', '|',
        'blockquote', 'codeBlock', 'horizontalRule', '|',
        'subscript', 'superscript', '|',
        'clearFormat', 'selectAll'
    ],
    'placeholder': 'Comece a escrever seu documento...',
    'content': '''
    <h1>Documento de Exemplo</h1>
    <p>Este é um editor de texto completo com todas as funcionalidades que você esperaria de um processador de texto moderno.</p>
    
    <h2>Funcionalidades Principais</h2>
    <ul>
        <li><strong>Formatação de texto</strong> - negrito, itálico, sublinhado</li>
        <li><em>Estilos de parágrafo</em> - cabeçalhos, listas, citações</li>
        <li>Inserção de <a href="#">links</a> e imagens</li>
        <li>Tabelas e outras estruturas</li>
    </ul>
    
    <blockquote>
        <p>"A escrita é a pintura da voz." - Voltaire</p>
    </blockquote>
    
    <p>Você pode criar tabelas:</p>
    <table>
        <tr>
            <th>Coluna 1</th>
            <th>Coluna 2</th>
            <th>Coluna 3</th>
        </tr>
        <tr>
            <td>Dados 1</td>
            <td>Dados 2</td>
            <td>Dados 3</td>
        </tr>
    </table>
    ''',
    'height': 'h-96',
    'editable': True,
    'word_count': True,
    'character_count': True,
    'spell_check': True,
    'auto_save': True
}

# Editor minimalista (como Medium)
text_editor_minimal = {
    'toolbar': ['bold', 'italic', 'link', 'heading2', 'heading3', 'bulletList', 'blockquote'],
    'placeholder': 'Conte sua história...',
    'content': '<h2>Título da História</h2><p>Era uma vez, em um tempo não muito distante...</p>',
    'height': 'h-80',
    'editable': True,
    'minimal_ui': True,
    'focus_mode': True
}

# Editor somente leitura (preview)
text_editor_readonly = {
    'toolbar': [],
    'content': '''
    <h1>Artigo Publicado</h1>
    <p class="text-gray-600 text-sm">Publicado em 15 de Janeiro, 2024 • 5 min de leitura</p>
    
    <p>Este é um exemplo de como o conteúdo aparece no modo somente leitura. Todo o texto está formatado e preserva a estrutura original.</p>
    
    <h2>Seção Principal</h2>
    <p>O editor preserva toda a formatação aplicada, incluindo <strong>texto em negrito</strong>, <em>texto em itálico</em> e <a href="#">links</a>.</p>
    
    <ul>
        <li>Lista com formatação</li>
        <li>Mantém a estrutura</li>
        <li>Exibe corretamente</li>
    </ul>
    ''',
    'height': 'h-64',
    'editable': False,
    'show_word_count': True
}

# Editor de código/markdown
text_editor_code = {
    'toolbar': ['bold', 'italic', 'code', 'codeBlock', 'link', 'bulletList', 'orderedList'],
    'placeholder': 'Digite seu markdown ou código...',
    'content': '''
# Título em Markdown

Este é um editor otimizado para **código** e *markdown*.

## Exemplo de código:

```python
def hello_world():
    print("Hello, World!")
    return True
```

- Item de lista
- Outro item
- `código inline`

> Citação em markdown
    ''',
    'height': 'h-80',
    'editable': True,
    'mode': 'markdown',
    'line_numbers': True,
    'syntax_highlighting': True
}

# Editor colaborativo
text_editor_collaborative = {
    'toolbar': ['bold', 'italic', 'underline', 'heading1', 'heading2', 'heading3', 'bulletList', 'orderedList', 'link', 'blockquote', 'comment'],
    'placeholder': 'Documento colaborativo...',
    'content': '''
    <h1>Documento Colaborativo</h1>
    <p>Este documento pode ser editado por múltiplos usuários simultaneamente.</p>
    
    <p>As alterações são sincronizadas em tempo real e você pode ver os cursores de outros usuários.</p>
    
    <h2>Comentários</h2>
    <p>Você também pode adicionar comentários para discussão.</p>
    ''',
    'height': 'h-80',
    'editable': True,
    'collaborative': True,
    'show_cursors': True,
    'comments_enabled': True,
    'version_history': True
}

# Configurações de toolbar
toolbar_options = {
    'formatting': ['bold', 'italic', 'underline', 'strike', 'code', 'subscript', 'superscript'],
    'headings': ['heading1', 'heading2', 'heading3', 'heading4', 'heading5', 'heading6'],
    'lists': ['bulletList', 'orderedList', 'taskList'],
    'alignment': ['textAlign:left', 'textAlign:center', 'textAlign:right', 'textAlign:justify'],
    'indentation': ['indent', 'outdent'],
    'colors': ['textColor', 'backgroundColor'],
    'links': ['link', 'unlink'],
    'media': ['image', 'video', 'audio'],
    'tables': ['table', 'addColumnBefore', 'addColumnAfter', 'deleteColumn', 'addRowBefore', 'addRowAfter', 'deleteRow'],
    'blocks': ['blockquote', 'codeBlock', 'horizontalRule'],
    'history': ['undo', 'redo'],
    'utility': ['clearFormat', 'selectAll', 'find', 'replace']
}

# Parâmetros do text editor
text_editor_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>content</code>', 'HTML', '-', 'Conteúdo inicial do editor'],
        ['<code>placeholder</code>', 'string', 'Digite aqui...', 'Texto de placeholder'],
        ['<code>toolbar</code>', 'array', '[]', 'Array com ferramentas da barra'],
        ['<code>height</code>', 'string', 'h-64', 'Altura do editor (classes CSS)'],
        ['<code>editable</code>', 'boolean', 'true', 'Se o editor está habilitado para edição'],
        ['<code>word_count</code>', 'boolean', 'false', 'Se mostra contador de palavras'],
        ['<code>character_count</code>', 'boolean', 'false', 'Se mostra contador de caracteres'],
        ['<code>spell_check</code>', 'boolean', 'true', 'Se ativa verificação ortográfica'],
        ['<code>auto_save</code>', 'boolean', 'false', 'Se salva automaticamente'],
        ['<code>minimal_ui</code>', 'boolean', 'false', 'Se usa interface minimalista'],
        ['<code>focus_mode</code>', 'boolean', 'false', 'Se ativa modo foco'],
        ['<code>collaborative</code>', 'boolean', 'false', 'Se ativa modo colaborativo'],
        ['<code>show_cursors</code>', 'boolean', 'false', 'Se mostra cursores de outros usuários'],
        ['<code>comments_enabled</code>', 'boolean', 'false', 'Se permite comentários'],
        ['<code>version_history</code>', 'boolean', 'false', 'Se mantém histórico de versões'],
        ['<code>mode</code>', 'string', 'wysiwyg', 'Modo: wysiwyg, markdown, code'],
        ['<code>line_numbers</code>', 'boolean', 'false', 'Se mostra números de linha'],
        ['<code>syntax_highlighting</code>', 'boolean', 'false', 'Se ativa highlight de sintaxe'],
        ['<code>max_length</code>', 'number', '-', 'Número máximo de caracteres'],
        ['<code>on_change</code>', 'string', '-', 'Callback para mudanças'],
        ['<code>on_save</code>', 'string', '-', 'Callback para salvamento'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados consolidados do text editor
TEXT_EDITOR_DATA = {
    'basic': text_editor_basic,
    'complete': text_editor_complete,
    'minimal': text_editor_minimal,
    'readonly': text_editor_readonly,
    'code': text_editor_code,
    'collaborative': text_editor_collaborative,
    'toolbar_options': toolbar_options,
    'params': text_editor_params,
} 