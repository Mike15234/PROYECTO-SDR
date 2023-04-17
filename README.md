# PROYECTO-SDR
Proyecto SDR 2023
Introduccion:

  Este proyecto del curso de Transmisores y Receptores en Radiocomunicaciones tiene como objetivo principal el diseño y construcción de un receptor de radio capaz de recibir una frecuencia de radio y transcribir el audio recibido. En este proyecto, se explorará cómo se reciben y cómo se decodifican las señales de audio en la frecuencia recibida. El resultado final será un receptor de radio funcional que pueda sintonizar y reproducir diversas estaciones de radio en la frecuencia deseada.

Además, se utilizará un servidor Apache2 para montar una página web donde se mostrará el texto transcrito de la radio recibida en tiempo real. De esta manera, los usuarios podrán leer el texto correspondiente a la transcripción del audio. Para implementar esta funcionalidad, se utilizarán tecnologías web como HTML, CSS y JavaScript. De esta manera, el proyecto no solo permitirá la recepción de audio, sino que también mejorará la experiencia de los usuarios a través de una página web interactiva y fácil de usar.

Frontend:
  1. Javascript
  2. HTML
  3. CSS

Backend:
  1. Python
  2. GNU Radio
  
Requerido:
  1. Lime SDR
  2. Visual Studio Code
  3. GNU Radio 
  4. Servidor Apache

Recomendaciones:
  1. Utilizar la tarjeta LimeSDR en un entorno abierto o con interferencias minimas.
  2. Sintonizar una frecuencia comercial sin mucho ruido o anuncios publicitarios en el top_block de GNU Radio.
  3. Verificar las direcciones de escritura en el codigo de VS Code (TxRx.py).

Procedimiento para utilizar el proyecto:
  1. Instalar el servidor Apache2. (Depende del sistema operativo la instalacion, en este caso se realiza en base a Ubuntu).
    Para ello debe abrir la terminal, realizar la accion update y luego con la siguiente linea de comando instalar el servidor: 
    
    sudo apt install apache2
    
  Luego puede ingresar a su navegador web y dirigirse al localhost para verificar si este se encuentra funcionando.
    
  2. Clonar el repositorio.
    Debe clonar el repositorio desde la branch 'master' donde se encuentran los codigos del proyecto, todo esto en una carpeta donde recuerde la direccion.
    
  3. Del repositorio clonado es requerido cargar el archivo HTML al servidor
    Para ello se puede utilizar el comando siguiente: 
    
    sudo cp -f ProyectoTxRx.html /var/www/html
   
  Una vez el archivo HTML se encuentra copiado de manera correcta en el servidor, al ingresar a su navegador e introducir la direccion "localhost/ProyectoTxRx.html", este deberia mostrar la pagina web con un titulo que diga "Contenido Archivo de Texto".
  
  4. Para comenzar a utilizar la transcripcion de texto debera iniciar los programas en el siguiente orden:
  
    a. Iniciar el top_block de GNU Radio para sintonizar la frecuencia deseada.
    b. Iniciar la pagina web en el localhost indicada anteriormente.
    c. Iniciar el codigo TxRx.py en VS Code para comenzar a recibir el audio de GNU Radio y enviar los datos de transcripcion al 
    archivo de texto que se mostrara en la pagina HTML.

