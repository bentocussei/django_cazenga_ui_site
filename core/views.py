from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "base.html")

def demo(request):
    # Dados para os tabs
    tabs_data = [
        {
            "id": "account", 
            "label": "Conta", 
            "content": "<div class='space-y-4'><h3 class='text-lg font-medium'>Configurações da Conta</h3><p>Gerencie suas informações pessoais e preferências de conta.</p></div>"
        },
        {
            "id": "password", 
            "label": "Senha", 
            "icon": "<svg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke-width='1.5' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' d='M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z' /></svg>", 
            "content": "<div class='space-y-4'><h3 class='text-lg font-medium'>Alterar Senha</h3><p>Atualize sua senha regularmente para manter sua conta segura.</p></div>"
        },
        {
            "id": "notifications", 
            "label": "Notificações", 
            "content": "<div class='space-y-4'><h3 class='text-lg font-medium'>Preferências de Notificação</h3><p>Escolha quais notificações você deseja receber.</p></div>"
        }
    ]
    
    context = {
        'tabs_data': tabs_data
    }
    return render(request, "demo.html", context)

def test(request):
    return render(request, "test.html")

def demo_simple(request):
    return render(request, "demo_simple.html")

def demo_especializado(request):
    return render(request, "demo_especializado.html")
