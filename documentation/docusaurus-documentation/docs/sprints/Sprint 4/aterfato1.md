---
title: Artefato - Interface Navegável
sidebar_position: 1
---
## Mockup

Um mockup de alta fidelidade é uma representação visual detalhada e próxima do produto final, utilizado para apresentar o visual e a experiência do usuário antes da implementação. Este tipo de mockup praticamente representa o visual definitivo da solução, permitindo avaliações precisas e feedback concreto antes da produção final. Suas vantagens incluem economia de tempo, facilitação da comunicação entre equipes e stakeholders, e a capacidade de identificar e corrigir problemas visualmente antes da implementação. Neste documento, evidenciaremos nosso processo de desenvolvimento da interface do usuário.

<div style={{ textAlign: 'center', padding: "0px" }}>
    <p style={{ margin: '15px', fontWeight: 'bold' }}>Para acessar e interagir com o Mockup desenvolvido <a href="https://www.figma.com/proto/73gPLi62HNx6Pj0WL5cGoJ/Arm-Group?page-id=28%3A42&type=design&node-id=279-350&viewport=-179%2C-169%2C0.07&t=dj4G99KuIqo1uJGd-1&scaling=scale-down&starting-point-node-id=279%3A350&show-proto-sidebar=1&mode=design" target="_blank">Clique aqui</a></p>
</div>

### Telas desenvolvidas
<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela incial</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 01 - Tela Inicial
    ![image](/img/mockup/TelaInicial.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta será a primeira tela apresentada ao usuário ao iniciar a aplicação. Seu principal objetivo é direcionar os dois tipos de usuários para suas respectivas áreas. O usuário farmacêutico será direcionado para sua área ao clicar no botão 'Farmacologista', enquanto o auxiliar de farmácia selecionará a opção 'Auxiliar de Farmácia'. A navegação é projetada de forma simples para garantir uma experiência sem complicações para o usuário.

---

<p style={{fontSize: '160%', fontWeight: 'bold' }}>Fluxo: Farmacêutico</p>
<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela principal - Farmacêutico</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 02 - Tela Principal - Farmacologista
    ![image](/img/mockup/TelaPrincipal.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela é a primeira que o usuário do perfil farmacêutico encontrará após selecionar sua área. Os kits de emergência são apresentados em uma disposição organizada, em formato de matriz, com botões representando cada modelo disponível. Ao clicar em um kit específico, o farmacêutico será redirecionado para outra tela com informações detalhadas sobre o kit selecionado.


Além disso, um header é visível na tela, contendo uma barra de pesquisa para facilitar a localização de kits desejados. Há também a opção de criar um novo modelo de kit, acessível através do botão 'Novo kit'

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela do Kit - Farmacêutico</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 03 - Tela do Kit - Farmacologista
    ![image](/img/mockup/TeladoKit.png)
    Fonte: Elaborado pelos próprios autores
</div>
Após selecionar um dos modelos de kit na tela principal, o farmacêutico será redirecionado para esta tela. Aqui, ele poderá visualizar todos os itens presentes no kit, juntamente com suas quantidades. Além disso, há a opção de editar o kit caso seja identificada alguma inconformidade. Para isso, basta selecionar o botão 'Editar Kit' no header.

Se não houver necessidade de alterações, o usuário pode retornar à tela principal utilizando o botão 'Voltar', também presente no header.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela de Edição de Kit - Farmacêutico</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 04 - Tela Edição de Kit - Farmacologista
    ![image](/img/mockup/EdiçãodeKit.png)
    Fonte: Elaborado pelos próprios autores
</div>
Após selecionar a opção 'Editar Kit', o usuário será redirecionado para esta tela. Embora seja muito semelhante à tela anterior, aqui é possível editar todos os itens presentes no kit. Para isso, basta clicar nos itens desejados, que estão disponíveis em uma lista.

Caso seja necessário adicionar um novo item ao kit, o usuário pode clicar no botão com o símbolo de '+'.

Após finalizar as modificações, o usuário pode salvar suas mudanças ao clicar em 'Concluir Edição', botão contido no header. No entanto, caso deseje cancelar suas alterações, basta clicar em 'Cancelar'.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela de Novo Kit - Farmacêutico</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 05 - Tela de Novo Kit - Farmacologista
    ![image](/img/mockup/NovoKit.png)
    Fonte: Elaborado pelos próprios autores
</div>
Esta tela é idêntica à tela de edição de kit, exceto pelo fato de que nenhum item está pré-registrado para edição. Portanto, todos os itens devem ser adicionados pelo usuário. O processo de adição de itens é realizado clicando no botão com o símbolo de '+'.

Após selecionar os itens desejados para o novo kit, o usuário pode salvar suas mudanças ao clicar em 'Concluir Edição', botão presente no header. Se o usuário preferir cancelar a criação do novo kit, basta clicar em 'Cancelar'.

---

<p style={{fontSize: '160%', fontWeight: 'bold' }}>Fluxo: Auxiliar</p>
<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela Principal - Auxiliar</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 06 - Tela Principal - Auxiliar
    ![image](/img/mockup/TelaPrincipal2.png)
    Fonte: Elaborado pelos próprios autores
</div>
Esta tela será a primeira vista pelo usuário que selecionar a área de Auxiliar de Farmácia. Assim como na tela principal do Farmacêutico, o usuário poderá visualizar todos os modelos de kits existentes. No entanto, há uma pequena diferença: ao lado dos botões dos kits, há um pequeno botão com o símbolo de '+'. Esse botão está relacionado à funcionalidade exclusiva desta tela, a 'Fila de Espera dos Kits'. Ao clicar neste botão, o usuário pode adicionar mais kits à fila de espera, bem como removê-los.

Além disso, na parte superior da tela, o usuário pode acessar o armazém clicando no botão 'Armazém'.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Tela do Kit - Auxiliar</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 07 - Tela do Kit - Auxiliar
    ![image](/img/mockup/TeladoKit2.png)
    Fonte: Elaborado pelos próprios autores
</div>
Esta tela é idêntica à tela de detalhes do kit para o farmacêutico, com a exceção de que não possui a opção 'Editar Kit'. Apenas os farmacêuticos têm autorização para realizar tais ações, tornando esta tela exclusivamente para visualização dos itens do kit pelo auxiliar de farmácia.

<p style={{fontSize: '130%', fontWeight: 'bold' }}>Armazém - Auxiliar</p>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 08 - Armazém - Auxiliar
    ![image](/img/mockup/Armazem.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela é muito semelhante à tela de detalhes do kit. No entanto, em vez de exibir os itens de um kit de emergência, ela mostra os itens disponíveis no armazém. O botão de edição do kit é substituído por um botão 'Reabastecido', utilizado para enviar ao sistema a informação de que o estoque foi reabastecido com sucesso.

---
 
 ### Especificações dos componentes utilizados
Nesta seção, você encontrará informações detalhadas sobre os principais componentes utilizados para a idealização do nosso mockup e, consequentemente, para o desenvolvimento da nossa interface. Aqui, exploraremos os elementos-chave que compõem a estrutura visual e funcionalidade do projeto.
 <div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 09, 10, 11 - Componentes em destaque
    ![image](/img/doc_component/component1.png)
</div>
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    ![image](/img/doc_component/component2.png)
</div>
<div style={{width: '40%', margin: '0 auto', textAlign: 'center'}}>
    ![image](/img/doc_component/component3.png)
    Fonte: Elaborado pelos próprios autores
</div>

Nesta seção, detalharemos cada elemento destacado anteriormente, descrevendo sua função, aparência e características gerais. A seguir, você encontrará uma análise minuciosa dos componentes que compõem nosso wireframe, permitindo uma compreensão abrangente de sua implementação e interação na interface.

<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 12 - Explicação de componentes
    ![image](/img/doc_component/componentExplanation.png)
    Fonte: Elaborado pelos próprios autores
</div>

---

## Frontend

O frontend não é nada mais que a versão final da nossa interface que será integrada à solução final e, portanto, deve ser 100% funcional. Com isso, o frontend é a parte da solução com a qual o cliente interagirá diretamente e conseguirá resolver suas dependências na plataforma. Neste tópico, iremos passar por cada tela que já começou a ser desenvolvida e abordaremos pontos específicos de cada uma delas.

Observação: As telas e o processo de integração da interface ao backend e ao sistema do braço robótico ainda estão em processo de desenvolvimento, portanto, ainda não se apresentam em seu estado final. Além do mais a maior parte das funcionalidades das telas já foram tratadas na descrição do Mockup acima e por isso nesse tópico será tratado apenas de forma mais específica a lógica por trás das telas.

---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 13 - Frontend: armazem.html
    ![image](/img/frontend/armazem.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta primeira tela representa a "Tela principal" do fluxo do Auxiliar que foi desenvolvida no Mockup.

**Lógica**:
- Ao clicar no botão Armazém, a rota "/reabastecimento" é chamada e o usuário é redirecionado para a tela do "Armazém" que contem todos os itens.

---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 14 - Frontend: config.html
    ![image](/img/frontend/config.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela representa um modal que será aberto ao editar algum item na "tela de edição de Kit" ou "Tela de novo kit" do fluxo do farmacêutico que estão presentes no Mockup. 

**Lógica**:
- Ainda não existe uma lógica de Rotas desenvolvida.
---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 15 - Frontend: kit.html
    ![image](/img/frontend/kit.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela representa a "Tela de Kit" do fluxo do Farmacêutico que foi desenvolvida no Mockup.

**Lógica**:
- Ao clicar no botão "Novo kit" a rota "/novoKit" é chamada e o usuário é redirecionado para a tela de "Novo Kit".
- Ao clicar no botão "Voltar" a rota "/telaP" é chamada e o usuário retorna para a tela "Principal".
---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 16 - Frontend: novoKit.html
    ![image](/img/frontend/novoKit.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela representa a "Tela de Novo Kit" do fluxo do Farmacêutico que foi desenvolvida no Mockup. 

**Lógica**:
- Ao clicar no botão "Cancelar" a rota "/telaP" é chamada e o usuário retorna para a tela "Principal".
- Ao clicar no botão "+" a rota "/kit" é chamada e aparece o modal de adição de novos itens".
- Rota para botão "Concluir edição" ainda em desenvolvimento.
---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 17 - Frontend: reabastecimento.html
    ![image](/img/frontend/reabastecimento.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela representa o "Armazém" do fluxo do Auxiliar que foi desenvolvida no Mockup. 

**Lógica**:
- Ao clicar no botão "Voltar" a rota "/auxiliar" é chamada e o usuário é redirecionado para a tela de "Principal" do fluxo do Auxiliar.
---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 18 - Frontend: telaExclusao.html
    ![image](/img/frontend/telaExclusao.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela representa um modal que será aberto tentar excluir algum modelo de kit na "Tela Principal" do fluxo do Farmacêutico que esta presente no Mockup. 

**Lógica**:
- Ao clicar no botão "Voltar" a rota "/telaP" é chamada e o usuário retorna para a tela "Principal".
- Rota para o botão "Excluir" ainda em desenvolvimento.
---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 19 - Frontend: telaIncial.html
    ![image](/img/frontend/telaInicial.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela representa a "Tela Incial", que é a Tela que vem antes da divisão de fluxos entre Auxiliar e Farmacêutico, que foi desenvolvida no Mockup. 

**Lógica**:
- Ao clicar no botão "Auxiliar" a rota "/auxiliar" é chamada e o usuário retorna para a tela "Principal" do fluxo do Auxiliar.
- Ao clicar no botão "Farmacologista" a rota "/farmacologista" é chamada e o usuário retorna para a tela "Principal" do fluxo do Farmacêutico.
---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 20 - Frontend: telaKit.html
    ![image](/img/frontend/telaKit.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela representa a "Tela de Kit" do fluxo do Farmacêutico que foi desenvolvida no Mockup. 

**Lógica**:
- Ainda não existe uma lógica de Rotas desenvolvida.
---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 21 - Frontend: telaP.html
    ![image](/img/frontend/telaP.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela representa a "Tela Principal" do fluxo do Farmacêutico que foi desenvolvida no Mockup. 

**Lógica**:
- Ao clicar no botão do kit referente a rota do kit selecionado é chamada e o usuário é redirecionado para a tela de tal kit.
- Ao clicar no botão com simbolo de lixeira a rota de exclusão do kit selecionado é chamada e o usuário é redirecionado par ao modal para confirmar a exclusão.
- Ao clicar no botão "Novo kit" a rota "/novoKit" é chamada e o usuário é redirecionado para a tela de "Novo Kit".

---
<div style={{width: '80%', margin: '0 auto', textAlign: 'center'}}>
    Imagem 22 - Frontend: config.html
    ![image](/img/frontend/visualizacaoKit.png)
    Fonte: Elaborado pelos próprios autores
</div>

Esta tela representa a "Tela de kit" do fluxo do Auxiliar que foi desenvolvida no Mockup. 

**Lógica**:
- Ao clicar no botão "Voltar" a rota "/auxiliar" é chamada e o usuário é redirecionado para a tela de "Principal" do fluxo do Auxiliar.
