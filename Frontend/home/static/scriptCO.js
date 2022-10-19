/*lectura y envio de mensajes de consumo*/
function leerArchivo(e) {
    var archivo = e.target.files[0];
    if (!archivo) {
        return;
    }
    var lector = new FileReader();
    lector.onload = function (e) {
        var contenido = e.target.result;
        enviarContenido(contenido);
    };
    lector.readAsText(archivo);
}

function enviarContenido(contenido) {
    console.log(contenido)

    fetch('http://127.0.0.1:3000/consumos', {
        method: 'POST',
        body: contenido,
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        }
    })

        .then(res => res.json())
        .catch(err => {
            console.error('Error:', err)
            swal("¡Error!", "¡Ha ocurrido un error!", "error");
        })
        /* ULTIMA TRANSFORMACION
            Si el metodo funciono correctamente y se logro transformar la respuesta en un JSON, hara lo que este dentro de las llaves.
        */
        .then(response => {
            let consumos = response.Consumos;
            swal("¡Correcto!", consumos + " consumos procesados correctamente", "success");
        })
}

document.getElementById('file-input')
    .addEventListener('change', leerArchivo, false); 