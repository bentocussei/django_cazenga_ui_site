# Estrutura Modular de Dados dos Componentes

Esta pasta contém os dados específicos para cada componente, organizados em arquivos separados para melhor manutenibilidade.

## Estrutura

```
core/data/
├── __init__.py          # Centralizador de importações
├── button_data.py       # Dados do componente Button
├── alert_data.py        # Dados do componente Alert
├── input_data.py        # Dados do componente Input
├── table_data.py        # Dados do componente Table
├── card_data.py         # Dados do componente Card
└── ...                  # Outros componentes
```

## Como usar

### Importação direta
```python
from core.data.button_data import BUTTON_PARAMS
from core.data.alert_data import ALERT_EXAMPLES, ALERT_PARAMS
```

### Importação centralizada
```python
from core.data import COMPONENT_DATA, BUTTON_PARAMS, ALERT_EXAMPLES
```

### Uso em views
```python
def component_detail(request, component_name):
    # Usando o mapeamento centralizado
    component_data = COMPONENT_DATA.get(component_name, {})
    
    context = {
        'params': component_data.get('params', {}),
        'examples': component_data.get('examples', []),
        # ...
    }
```

## Padrão para novos componentes

Para criar dados para um novo componente:

1. Criar arquivo `{component}_data.py`
2. Definir constantes seguindo o padrão:
   - `{COMPONENT}_PARAMS` - parâmetros do componente
   - `{COMPONENT}_EXAMPLES` - exemplos de uso
   - `{COMPONENT}_DATA` - dados específicos (opções, items, etc.)

3. Atualizar `__init__.py` com as importações
4. Adicionar ao `COMPONENT_DATA` para acesso centralizado

## Exemplo de arquivo de componente

```python
"""
Dados específicos para o componente Example
"""

EXAMPLE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>prop1</code>', 'string', '-', 'Descrição da propriedade'],
        # ...
    ]
}

EXAMPLE_EXAMPLES = [
    {'variant': 'default', 'text': 'Exemplo'},
    # ...
]
```

## Vantagens desta estrutura

1. **Organização**: Cada componente tem seus dados isolados
2. **Manutenibilidade**: Fácil de encontrar e editar dados específicos
3. **Reutilização**: Importação granular conforme necessário
4. **Escalabilidade**: Fácil adicionar novos componentes
5. **Legibilidade**: Código mais limpo e organizado 