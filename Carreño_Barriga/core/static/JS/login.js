async function login()
		{
			var usuario = document.getElementById("usuario").value;
			var Contraseña = document.getElementById("pass").value;

			if(usuario == "adminCB" && Contraseña == "3254")
			{
				alert("Usuario y Contraseña validos");
                window.location.href="principal";
			}
			if (usuario == "" && Contraseña == ""){
				alert("Error de las Credenciales") 
				
		}
	}


//         document.getElementById("Login").addEventListener("click", login);

// async function login(){

//     const email = document.getElementById('EmailTxt').value;
//     const password = document.getElementById('PasswordTxt').value;
//     const divError = document.getElementById('divError')
//     if(email == 'adminCB' || password == '3254'){
       
//     }
//     else (email == '' || password == '')
//     {
//         divError.setAttribute("class", "alert alert-danger")
//         divError.setAttribute("role", "alert")
//         divError.innerHTML = "Error debe llenar los campos"
//         return;
//     }
// }

