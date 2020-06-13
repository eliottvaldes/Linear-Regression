"""
Created on Mon Jun  8 01:25:45 2020

@author: Eliot
"""
import pandas as pd
import webbrowser
parametros = pd.read_csv("datos_.csv")
df = pd.DataFrame(parametros)

#Script para regresion linear
scriptrl = ""
i=0
while i<5149:
        scriptrl = scriptrl+"{x:'"+str(parametros['Periodo'].loc[i])+"', y:"+str(parametros['Monto'].loc[i])+"},\n"
        i+=10

#LOS DATOS TOTALES SON:5149, VAN DESDE 03/01/2000 HASTA 12/06/2020 
#Script que obtiene todos los datos, desde el 2000 al 2020 
#El nombre del script es "script+periodo a graficar" en este caso es el periodo 1 del 2000 al 2020
scriptp1 = ""
i=0
while i<5149:
        scriptp1 = scriptp1+"{x:'"+str(parametros['Fecha'].loc[i])+"', y:"+str(parametros['Monto'].loc[i])+"},\n"
        i+=1

#script que obtiene datos solamente desde el 2000 al 2010
scriptp2 = ""
ii=0
while ii<2520:
        scriptp2 = scriptp2+"{x:'"+str(parametros['Fecha'].loc[ii])+"', y:"+str(parametros['Monto'].loc[ii])+"},\n"
        ii+=1
        
#script que obtiene datos solamente desde el 2010 al 2020
scriptp3 = ""
iii=2520
while iii<5149:
        scriptp3 = scriptp3+"{x:'"+str(parametros['Fecha'].loc[iii])+"', y:"+str(parametros['Monto'].loc[iii])+"},\n"
        iii+=1
        
#Este script obtiene datos de inicios desde 02/01/2020 hasta 12/06/2020 
scriptp4 = ""
iiii=5035
while iiii<5149:
        scriptp4 = scriptp4+"{x:'"+str(parametros['Fecha'].loc[iiii])+"', y:"+str(parametros['Monto'].loc[iiii])+"},\n"
        iiii+=1
        
#Estas son imagenes de graficas simples generadas con pandas
#df.groupby('Fecha')['Monto'].sum().plot(kind='bar',legend='Reverse')
#df.groupby('Periodo')['Monto'].sum().plot(kind='line',legend='Reverse')
#df.groupby('Periodo')['Monto'].sum().plot(kind='area',legend='Reverse')


#Este es el documento que va a abrir
page= open('index.php','w')

#Aquí comienza el html
mensaje = """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.2/raphael-min.js"></script>
    <script src="assets/js/morris.js"></script>  
    <script src='assets/js/morris.min.js'></script>
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.2/raphael-min.js"></script> 
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/export-data.js"></script>
    <script src="https://code.highcharts.com/modules/accessibility.js"></script>
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/example.css">  
    <link rel="stylesheet" href="assets/css/morris.css">
    <link rel="stylesheet" href="assets/css/fontawesome.css">
    <title>REGRESION LINEAL</title>
</head>
<body> 
    <div class="container">   
        <hr>  
            <h1 align="center"><i class="fa fa-money"></i> PESO vs DOLAR <i class="fa fa-money"></i></h1>
        <hr>
        <div class="row" >              
            <figure class="highcharts-figure">
                <div id="grl"></div>
            </figure>
            
        </div>
        <br>
        <div>
            <div class="help-box">
                <ul>
                    <li> <a data-toggle="modal" data-target="#myModalp" > <button type="button" name="button" class="btn btn-success">PREDICCION <i class="fa fa-dollar"></i></button></a> </li>                    
                    <li> <a data-toggle="modal" data-target="#myModaln" > <button type="button" name="button" class="btn btn-success">NOTAS <i class="fa fa-book"></i></button></a> </li>                    
                    <li> <a data-toggle="modal" data-target="#myModalf" > <button type="button" name="button" class="btn btn-success">FlUCTUACION <i class="fa fa-level-down"></i></button></a> </li>                    
                </ul>
                <br>
                <ul>
                    <li><button type="button" class="btn btn-warning my-5" onclick='grafica1()'> Grafica Global <i class="fa fa-pie-chart"></i></button></li>
                    <li><button type="button" class="btn btn-primary my-5" onclick='grafica2()'> Grafica 2000-2010 <i class="fa fa-area-chart"></i></button></li>
                    <li><button type="button" class="btn btn-danger my-5" onclick='grafica3()'> Grafica 2010-2020 <i class="fa fa-line-chart"></i></button></li> 
                    <li><button type="button" class="btn btn-info my-5" onclick='grafica4()';'graficar4()'> Grafica 2020 <i class="fa fa-bar-chart"></i></button></li> 
                </ul>
            </div>    
        </div>
        
            <!-- Modal window prediction-->            
            <div class="modal fade lug" id="myModalp" role="dialog">
                <div class="modal-dialog">
                   <!-- Modal content-->
                   <div class="modal-content">
                      <div class="modal-header">
                         <button type="button" class="close" data-dismiss="modal">&times;</button>
                         <h4 class="modal-title">PREDICCION <i class="fa fa-level-up"></i></h4>
                      </div>
                      <div class="modal-body">                         
                            <p><h4>EL PRECIO DEL PESO EN 5 ANOS (13/06/2025) sera de: <u><br>$22.85949654</u><br></h4></p>                                             
                            <br>
                            <br>
                            <p>
                            <h4>
                                (1/5149)= 1 dia <u>Desde 03/01/2000 Hasta 12/06/2020</u> <br> 
                                <br>Ecuacion:y = 0.0021x + 7.8731 <br>
                                <br>R^2 = 0.8203 <br>
                                <br>Promedio:$13.39 <br>
                                <br>Color Azul: Valor menor al promedio <br>
                                <br>Color Verde: Valor mayor o igual al promedio <br>
                            </h4>
                        </p>
                        <br>
                        <span>
                            <button type="button" class="close" data-dismiss="modal">Cerrar &times;</button>
                        </span>
                        <br>                        
                      </div>
                   </div>
                   
                </div>             
            </div>
            
            <!-- Modal window notes-->
            <div class="modal fade lug" id="myModaln" role="dialog">
                <div class="modal-dialog">
                   <!-- Modal content-->
                   <div class="modal-content">
                      <div class="modal-header">
                         <button type="button" class="close" data-dismiss="modal">&times;</button>
                         <h4 class="modal-title"><i class="fa fa-bookmark"></i> NOTAS  </h4>
                      </div>
                      <div class="modal-body">
                      <!-- TABLA 1 PARA MOSTRAR LOS DATOS OBTENIDOS EN LA REGRESION LINEAL que pertenecen al csv-->            
                        <table class="table table-hover table-bordered">
                                <caption>Estadisticas globales</caption>
                                <thead">
                                  <tr>
                                    <th scope="col"> </th>
                                    <th scope="col">Periodo</th>
                                    <th scope="col">Precio por dolar</th>            
                                  </tr>
                                </thead>
                                <tbody>
                                  <tr>
                                    <th scope="row">Count</th>
                                    <td> 5149.000000 </td>
                                    <td> 5149.000000 </td>
                                  </tr>
                                  <tr>
                                    <th scope="row">Mean</th>
                                    <td> 2575.000000 </td>
                                    <td> 13.392137 </td>
                                  </tr>
                                  <tr>
                                    <th scope="row">Std</th>
                                    <td> 1486.532599 </td>
                                    <td> 3.531484 </td>
                                  </tr>
                                  <tr>
                                    <th scope="row">Min</th>
                                    <td> 1.000000 </td>
                                    <td> 8.942800 </td>
                                  </tr>
                                  <tr>
                                    <th scope="row">25%</th>
                                    <td> 1288.000000 </td>
                                    <td> 10.818000 </td>
                                  </tr>
                                  <tr>
                                    <th scope="row">50%</th>
                                    <td> 2575.000000 </td>
                                    <td> 12.604800 </td>
                                  </tr>
                                  <tr>
                                    <th scope="row">75%</th>
                                    <td> 3862.000000 </td>
                                    <td> 15.351700 </td>
                                  </tr>
                                  <tr>
                                    <th scope="row">Max</th>
                                    <td> 5149.000000 </td>
                                    <td> 25.118500 </td>
                                  </tr>
                                </tbody>                        
                        </table>
                        <br>
                        <!-- TABLA PARA MOSTRAR LOS DATOS OBTENIDOS EN LA REGRESION LINEAL-->            
                        <table class="table table-hover table-bordered">
                            <caption>Datos de regresion lineal</caption>
                            <thead class="thead-dark">
                              <tr>
                                <th scope="col">Coefficients</th>
                                <th scope="col">Mean squared error</th>
                                <th scope="col">Variance score</th>            
                              </tr>
                            </thead>
                            <tbody>
                                <tr>                
                                    <td> [0.00215167] </td>  
                                    <td> 2.24 </td>         
                                    <td> 0.82 </td>
                                  </tr>        
                            </tbody>
                        </table>                      
                        <br>
                        <!-- BOTON QUE LLEVA A PAGINA DONDE ESTÁ EL CODIGO DE EL PROGRAMA QUE GRAFICA LA REGRESION LINEAL-->            
                            <a href="rl_code.php" class="btn btn-danger btn-lg active" role="button" aria-pressed="true">Codigo de Regresion Lineal</a>
                        <br>
                       <button type="button" class="close" data-dismiss="modal">Cerrar &times;</button>
                       <br> 
                       
                     </div>
                   </div>
                </div>             
            </div>
            
            <!-- Modal window fluctuation-->            
            <div class="modal fade lug" id="myModalf" role="dialog">
                <div class="modal-dialog">
                <!-- Modal PARA MOSTRAR LAS RAZONES DE FLUCTIACINO-->
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title">FLUCTUACION <i class="fa fa-level-down"></i></h4>
                        </div>
                        <div class="modal-body">                         
                            <p>                                             
                            En Estados Unidos, el Sistema de la Reserva Federal (FED, por sus siglas en ingles), influye en el precio y la circulacion de esta divisa, establece las politicas monetarias y es la encargada de determinar cuanto dinero debe estar en circulacion y los rangos previos de inflacion.
                            <br>
                            En Mexico el tipo de cambio peso-delar se determina bajo un regimen cambiario de libre flotacion. Es la Comision de Cambios la que faculta al Banco de Mexico para llevar a cabo operaciones en el mercado cambiario.
                            <br>
                            Otro factor que determina el tipo de cambio peso-dolar es la ley de oferta y la demanda, y es tan simple como el hecho de que cuando la divisa es escasa sube de precio ya sea por su alta demanda o porque hay poca comparada con otras divisas. En el caso de la depreciacion es porque existe demasiada oferta de la misma o porque es abundante en relacion a otras.
                            <br>
                            Algunas otras razones de el aumento de el Dolar:
                            <br>
                            <ul>
                                <li>EL PRECIO DEL PETROLEO</li>
                                <li>CALENDARIO TRIBUTARIO</li>
                                <li>INVERSION EXTRANGERA Y DE PORTAFOLIO</li>
                                <li>LA CUENTA CORRIENTE DEL PAIS</li>
                            </ul>
                            <br>
                            Algunos datos historicos que contribuyeron a una mayor fluctuacion:
                            <br>
                                <ul>
                                    <li>1977 - Por combate a la deuda externa (DESCENSO)</li>
                                    <li>1978 - 1982  Devaluacion del peso (AUMENTO)</li>
                                    <li>1978 - 1982  Devaluacion del peso (AUMENTO)</li>
                                    <li>1994 - Error de diciembre (AUMENTO)</li>
                                    <li>1990 - Acuerdo comercial TLC  (DESCENSO)</li>
                                    <li>2008 - 2009 Gran recesion (AUMENTO )</li>
                                    <li>2014 - 2016 Depreciacion del costo del petroleo  (AUMENTO)</li>
                                    <li>2020 - Pandemia por COVID-19  (DESCENSO)</li>
                                </ul>
                            <br><br>
                            <span class="text-muted">
                                Fuentes:
                                <ul>
                                    <li><a href="https://www.banxico.org.mx/tipcamb/main.do?page=tip&idioma=sp">Banco de Mexico</a></li>
                                    <br><li><a href="https://www.bbva.com/es/factores-marcan-comportamiento-dolar/">BBVA page</a></li>
                                    <br><li><a href="https://www.nexos.com.mx/?p=4042">Nexos.com</a></li>
                                    <br><li><a href="https://www.eumed.net/cursecon/ecolat/mx/2017/devaluaciones-peso-mexico.html#:~:text=De%20esta%20manera%20fue%20como,d%C3%B3lar%20en%20mayo%20de%201913">Eumed.net</a></li>
                                    <br><li><a href="http://www.mexicomaxico.org/Voto/SobreVal02.htm">Mexicomaxico.org</a></li>
                                    <br><li><a href="https://mx.investing.com/currencies/usd-mxn-chart">Investing.com</a></li>
                                </ul>
                            </span>
                            </p>
                            <br>
                            <br>
                            <br>
                            <span>
                            <button type="button" class="close" data-dismiss="modal">Cerrar &times;</button>
                            </span>
                            <br>                        
                        </div>
                    </div>
                </div>             
            </div>

        <br>
        <hr>
        
        <div class="row" display:"inline-block">  
            <div class="col-md">                
                <h2>GRAFICA <i class="fa fa-pie-chart"></i> <span class="text-muted"> (2000-2020) </span></h2>
                <div id="RLP1"></div>
            </div>            
        </div>
        <div></div>        
        <hr>
        <div class="row" display:"inline-block">  
            <div class="col-md">                
                <h2>GRAFICA <i class="fa fa-area-chart"></i><span class="text-muted"> (2000-2010) </span></h2>
                <h4 class"text-muted"></h4>
                <div id="RLP2"></div>
            </div>            
        </div>
        <div></div>        
        <hr>
        <div class="row" display:"inline-block">  
            <div class="col-md">                
                <h2>GRAFICA <i class="fa fa-line-chart"></i><span class="text-muted"> (2010-2020) </span></h2>
                <div id="RLP3"></div>
            </div>            
        </div>
        <div></div>   
        <hr>
        <div class="row" display:"inline-block">  
            <div class="col-md">
                <h2>GRAFICA <i class="fa fa-bar-chart"></i><span class="text-muted"> (Enero 2020 - Junio 2020) </span></h2>
                <div id="RLP4"></div>
            </div>            
        </div>
        <div></div>   
        <hr>
    </div>
    
    
    <!--AQUI COMIENZAN TODOS LOS SCRIPTS PARA GRAFICAR -->
    
    
    <script>    
        function grafica1(){
            swal("Estamos trabajando en tu grafica!", {
            text: 'Nos demoraremos algunos segundos. Por favor no te desesperes',
            icon: "success",
            buttons: false,
            timer: 10000,
            });
            setTimeout("graficar1()", 50);
        }
        function graficar1(){
            Morris.Bar({
                element: 'RLP1',
                data: [
                    """+scriptp1+"""
                ],
                xkey: 'x',
                ykeys: ['y'],
                labels: ['Precio: $'],
                resize: true,
                barColors: function (row, series, type) {
                    if (type === 'bar') {
                    var red = Math.ceil(255 * row.y / this.ymax);
                    return 'rgb(' + red + ',0,0)';
                    }
                    else {
                    return '#000';
                    }
                }
            });  
        } 
    </script>
        
    <script>
        function grafica2(){
            swal("Estamos trabajando en tu grafica!", {
            text: 'Nos demoraremos algunos segundos. Por favor no te desesperes',
            icon: "success",
            buttons: false,
            timer: 6500,
            });
            setTimeout("graficar2()", 50);    
        }    
        function graficar2(){
            Morris.Bar({
                element: 'RLP2',
                behaveLikeLine: true,
                data: [
                """+scriptp2+"""
                ],
                xkey: 'x',
                ykeys: ['y'],
                labels: ['Precio: $'],
                resize:'true',
                barColors: function (row, series, type) {
                    if (type === 'bar') {
                    var blue = Math.ceil(106 * row.y / this.ymax);
                    return 'rgb(' + blue + ',145,187)';
                    }
                    else {
                    return '#000';
                    }
                }
            });
        }        
    </script>
    
    <script>
        function grafica3(){
            swal("Estamos trabajando en tu grafica!", {
            text: 'Nos demoraremos algunos segundos. Por favor no te desesperes',
            icon: "success",
            buttons: false,
            timer: 6500,
            });
            setTimeout("graficar3()", 50);
        }
        function graficar3(){
            
            Morris.Bar({
                element: 'RLP3',
                data:  [
                """+scriptp3+"""
                        ],
                xkey: 'x',
                ykeys: ['y'],
                labels: ['Precio: $'],
                axes:true,
                resize:true,
                barColors: function (row, series, type) {
                    if (type === 'bar') {
                    var green = Math.ceil(80 * row.y / this.ymax);
                    return 'rgb(' + green + ',193,44)';
                    }
                    else {
                    return '#000';
                    }
                }
            });    
        }
    </script>
    
    <script>
            function grafica4(){
                    swal("Estamos trabajando en tu grafica!", {
                    text: 'Nos demoraremos algunos segundos. Por favor no te desesperes',
                    icon: "success",
                    buttons: false,
                    timer: 1500,
                    });    
                    setTimeout("graficar4()", 50);
                    
            }
            function graficar4(){  
                Morris.Bar({
                element: 'RLP4',
                data:  [
                """+scriptp4+"""
                        ],                
                xkey: 'x',
                ykeys: ['y'],
                labels: ['Precio: $'],
                axes:true,  
                resize:true,
                barColors: function (row, series, type) {
                    if (type === 'bar') {
                    var violet = Math.ceil(234 * row.y / this.ymax);
                    return 'rgb(' + violet + ',104,224)';
                    }
                    else {
                    return '#000';
                    }
                    }
                });    
            };//Fin de funcion graficar4
            
    </script>
    
    <script>
        Highcharts.chart('grl', {
          title: {
          text: 'Regresion lineal'
          },
          xAxis: {
          min: -0.5,
          max: 5200
          },
          yAxis: {
            min: 0,
            max: 40
          },
         series: [{
            type: 'line',
            name: 'Regresion lineal',
            data: [[1, 9.3949], [7152, 22.85949654]],
            marker: {
              enabled: false
            },
        states: {
            hover: {
            lineWidth: 0
            }
        },
        enableMouseTracking: false
        }, {
        type: 'scatter',
        name: 'Costo del dolar',
        
        //Aqui van los datos que se extraen del archivo de datos.csv
        
        data: [
        """+scriptrl+"""
        ],
        marker: {
          radius: 4
        }
      }]
    });
    </script>


    <!--ESTOS SON ARCHIVOS PARA QUE FUNCIONEN LAS VENTANAS MODALES-->
    <!--main js--> 
    <script src="assets/js/jquery-1.12.4.min.js"></script> 
    <!--bootstrap js--> 
    <script src="assets/js/bootstrap.min.js"></script> 

</body>
</html>"""
page.write(mensaje)
page.close()
#Esta es la pagina que va a abrir y reescribir 
webbrowser.open_new_tab('index.php')