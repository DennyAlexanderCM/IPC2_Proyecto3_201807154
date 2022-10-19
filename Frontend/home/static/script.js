function reset() {
    fetch('http://127.0.0.1:3000/restablecer', {
        method: 'GET',
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
        .then(response => {
            console.log(response);
            valor = response.Mensaje
            swal("¡Correcto!", valor, "success");
        })
}