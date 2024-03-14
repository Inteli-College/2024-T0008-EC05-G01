---
title: Artefato - Hardware Periférico
sidebar_position: 1
---

# Por que escolhemos utilizar um periferico em nossa solução:

&emsp;Os periféricos desempenham um papel crucial em nossa solução IOT. Embora não sejam elementos essenciais para o funcionamento do sistema, eles contribuem significativamente para aumentar a qualidade e a eficiência das tarefas executadas. Ao integrar periféricos em nossa solução, elevamos a assertividade e garantimos um serviço de maior qualidade.

# Qual periférico escolhemos e por que:

&emsp;Optamos por integrar o sensor seguidor de linha TCRT5000, conhecido como sensor infravermelho, em nossa solução. Este periférico desempenha um papel fundamental ao garantir que o braço robótico execute suas tarefas com precisão. Ele atua como um mecanismo de verificação para a garra/ventosa acoplada à ponta do braço robótico. Se o sensor detectar a presença de material coletado, o processo continua normalmente. No entanto, caso não haja material identificado, o robô emite um aviso sonoro e executa a última tarefa atribuída a ele. Essa abordagem garante que os medicamentos sejam adequadamente coletados pela garra, minimizando possíveis divergências durante a montagem do kit médico.

## Demosntração visual do sensor TCRT5000:

<div style={{width: '40%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Sensor TCRT5000</p>
    ![image](/img/sensor-TCRT5000.jpg)
    <p>Fonte: disponível em <a href="https://www.google.com/url?sa=i&url=https%3A%2F%2Fmultilogica-shop.com%2Fprodutos%2Fsensor-optico-reflexivo-tcrt5000%2F&psig=AOvVaw0ij8kY8Xv2yhGNaDbbbAjY&ust=1710353065062000&source=images&cd=vfe&opi=89978449&ved=0CBUQjhxqFwoTCMCj0tOq74QDFQAAAAAdAAAAABAE" target="_blank">clique aqui</a></p>
</div>

# Quais componentes compõem nosso circuito junto ao periférico:

&emsp;Para a construção do nosso circuito e utilização do periférico, estamos utilizando os seguintes componentes descritos na tabela abaixo:

<div style={{width: '40%', margin: '0 auto', textAlign: 'center'}}>
    <p>Tabela xx - Listagem dos componentes</p>
    <table>
        <thead>
            <tr>
                <th>Componente</th>
                <th>Quantidade</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>LED vermelho</td>
                <td>1 unidade</td>
            </tr>
            <tr>
                <td>Sensor seguidor de linha TCRT5000</td>
                <td>1 unidade</td>
            </tr>
            <tr>
                <td>Resistor de 330 Ω</td>
                <td>3 unidades</td>
            </tr>
            <tr>
                <td>Jumper macho-macho</td>
                <td>9 unidades</td>
            </tr>
            <tr>
                <td>Placa Raspberry Pi Pico</td>
                <td>1 unidade</td>
            </tr>
            <tr>
                <td>Protoboard</td>
                <td>1 unidade</td>
            </tr>
        </tbody>
    </table>
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;A partir desses componentes é possível montar nosso circuito para a utilização do periférico TCRT5000.

# Guia de montagem:

&emsp;Placa que estamos utilizando para a construção do nosso circuito e seus respectivos pinos:

<div style={{width: '75%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Representação das portas da placa</p>
    ![image](/img/picow-pinout.svg)
    <p>Fonte: disponível em <a href="https://murilo-zc.github.io/M5-Inteli-Eng-Comp/Material/Semana-05/instrucao53/#41-apresenta%C3%A7%C3%A3o-da-forma-de-programar-o-raspberry-pi-pico-em-python" target="_blank">clique aqui</a></p>
</div>

&emsp;Realize a conexão entre o GND e a saída de 3V3 da placa na protoboard para poder energizar o circuito, estamos usando a o pino xx para a saída de energia e o pino xx para o GND:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Conexão das saídas da placa a protoboard</p>
    ![image](/img/conexao-positivo-negativo-placa.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;Agora, iremos ligar a o outro lado da placa, da seguinte maneira:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Conexão da protoboard inteira</p>
    ![image](/img/conexao-positivo-negativo.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;1- Agora que a protoboard está energizada corretamente, o primeiro passo para começar a construir nosso circuito é encaixar a placa Raspberry Pi Pico na protoboard com cuidado como mostra a imagem abaixo:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Montagem da Raspberry Pi Pico na protoboard</p>
    ![image](/img/placa-protoboard.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;2- Agora iremos realizar a montagem do nosso led vermelho ao circuito. Será necessário nessa etapa:

&emsp;&emsp;- 1 Resistor de 330 Ω

&emsp;&emsp;- 2 Jumper's macho-macho

&emsp;• Para melhor entedimento de como posicionar o LED em nossa protoboard vamos visualizar como funciona os terminas de um led observando a seguinte imagem:

<div style={{width: '70%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Exemplo de um LED e seus terminais</p>
    ![image](/img/led-exemplo.png)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;• Realize o posicionamento do led na protoboard da seguinte maneira:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Posicionamento do LED na protoboard</p>
    ![image](/img/led-placa-protoboard.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;• Agora conecte um dos terminas do resistor no terminal negativo do LED:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Conexão entre o terminal negativo do LED e o resistor</p>
    ![image](/img/led-resistor.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;• Conecte o LED ao GND da protoboard:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Conexão entre o terminal negativo do LED e o GND da protoboard</p>
    ![image](/img/led-gnd.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;• Agora basta ligar o terminal positivo do nosso LED a uma porta lógica que faça referência em seu código, aqui em nosso circuito estamos utilizando a porta lógica número xx:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Conexão do terminal positivo do LED a uma porta lógica da placa</p>
    ![image](/img/conexão-pl-final-led.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;• Aqui estamos conectando o terminal positivo do LED a porta lógica da placa número xx:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Conexão do terminal positivo do LED a uma porta lógica da placa parte 2</p>
    ![image](/img/conexão-pl-led.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;3- Agora iremos montar o nosso sensor TCRT5000, primeiro passo, é conecta-lo na protoboard dessa forma:

&emsp;• Realize o posicionamento do sensor na protoboard da seguinte maneira:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Posicionamento do sensor na protoboard</p>
    ![image](/img/posicionamento-infra.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;• Primeiro iremos conectar um dos lados do sensor ao resistor dessa maneira:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Posicionamento do resistor na protoboard</p>
    ![image](/img/resistor-infra.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;• Agora precisamos conectar o ground (GND) a um terminal do nosso sensor:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Posicionamento do GND do sensor na protoboard</p>
    ![image](/img/conexao-infra-gnd.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;• Iremos replicar esses ultimos dois passos para o outro lado do sensor:    

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Posicionamento do resistor na protoboard</p>
    ![image](/img/resistor-infra.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Posicionamento do GND do sensor na protoboard</p>
    ![image](/img/conexao-infra-gnd.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;• E por ultimo, iremos conectar o sensor a nossa porta lógica xx na placa, da seguinte forma:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Posicionamento do sensor em uma porta lógica na placa</p>
    ![image](/img/conexao-pl-infra.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Posicionamento final do sensor na protoboard</p>
    ![image](/img/conexa-final-infra.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

# Circuito ao terminar sua montagem:
&emsp;E por fim, nosso circuito deve estar parecido com algo assim no final de sua montagem (a placa está separada, entretando as conexões que levam até ela estão posicionadas da mesma maneira descrita):

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem xx - Montagem final do circuito</p>
    ![image](/img/circuito-final.jpeg)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;A compreensão da montagem do circuito deve ficar clara ao encarregado por seguir o passo a passo, caso seja necessário melhor entendimento do circuito se a documentação não tiver ficado clara, entre em contato com a seguinte organização que representa o grupo ARM <a href="https://www.linkedin.com/school/inteli-edu/mycompany/" target="_blank">clicando aqui</a>