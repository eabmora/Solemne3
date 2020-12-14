$(document).ready(function () {
    $('form[name="formContacto"]')
        .validate({
            errorElement: 'span',
            errorPlacement: function (error, element) {
                error.addClass('invalid-feedback');
                element.closest('.form-group').append(error);
            },
            highlight: function (element, errorClass, validClass) {
                $(element).addClass('is-invalid');
            },
            unhighlight: function (element, errorClass, validClass) {
                $(element).removeClass('is-invalid');
            },

            submitHandler: function() {
                let txtTitulo = $('#txtTitulo');
                let txtNombre = $('#txtNombre');
                let txtEmail = $('#txtEmail');
                let txtNumeroContacto = $('#txtNumeroContacto');
                let txtMensaje = $('#txtMensaje');

                axios.post('http://localhost:8000/contacto/Contacto/',
                    {
                        titulo: txtTitulo.val(),
                        nombre: txtNombre.val(),
                        email: txtEmail.val(),
                        numeroTelefono: txtNumeroContacto.val(),
                        mensaje: txtMensaje.val(),
                        estado: 'Recibido'
                    }).then((respuesta) => {
                        $('#formSuccess').show();
                        console.log(respuesta);
                    }).catch((error) => {
                        console.error(error);
                    })

            },

            rules: {

                txtTitulo: {
                    required: true
                },

                txtNombre: {
                    required: true
                },
                txtEmail: {
                    required: true,
                    email: true
                },
                txtNumeroContacto: {
                    required: true,
                    number: true
                }
            },
            messages: {

                txtTitulo: {
                    required: 'El campo de titulo es requerido'
                },

                txtNombre: {
                    required: 'El campo del nombre es requerido'
                },
                txtEmail: {
                    required: 'El campo del correo es requerido',
                    email: 'El campo del correo no tiene un formato válido de correo'
                },
                txtNumeroContacto: {
                    required: 'Ingrese su numero telefonico',
                    number: 'Solo caracteres numericos'

                }
            }
        })
})

