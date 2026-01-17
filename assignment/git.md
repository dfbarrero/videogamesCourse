# Lab 1: Primer contacto con Git y GitHub

## Objetivos 
- Primer contacto con Git y GitHub
- Conocer los casos de uso más habituales con Git/GitHub

>[!NOTE]blablabla

## Puesta a punto del entorno de trabajo
blablablabla

## Escenario 1: Crear un repositorio nuevo desde GitHub
blablablabla

``` mermaid
architecture-beta
    group api(cloud)[API]

    service db(database)[Database] in api
    service disk1(disk)[Storage] in api
    service disk2(disk)[Storage] in api
    service server(server)[Server] in api

    db:L -- R:server
    disk1:T -- B:server
    disk2:T -- B:db
    
    group api2(cloud2)[API2]

    service db2(database)[Database] in api2
    service disk12(disk)[Storage] in api2
    service disk22(disk)[Storage] in api2
    service server2(server)[Server] in api2

    db2:L -- R:server2
    disk12:T -- B:server2
    disk22:T -- B:db2
```

### Blablabla
asdfasdf

``` mermaid
flowchart LR
    A(etiqueta)-->B
    B-->C
    C-->D
    D-->E
    
    A-->E
```


## Escenario 2: Clonar un repositorio existente en GitHub
blablablabla

## Escenario 3: Partir de un proyecto sin control de versiones previo
blablablabla