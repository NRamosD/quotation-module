import React from 'react';
import './css/style.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUnlock, faUser } from '@fortawesome/free-solid-svg-icons'
 
function Log(){

    return(
        <body>
            <h1>Tracto tren</h1>
            <div className="login-form">
                 <h2>Acceder</h2>
                 <form action="#" method="POST">
                     <div className="form-group">
                        <label>Nombre de usuario:</label>
                        <div className="group">
                            <FontAwesomeIcon icon={faUser} color="#FC3955" pull="left" size="lg" />
                            <input type="text" className="form-control" placeholder="Nombre de usuario" required="required" />
                        </div>
                     </div>
                 </form>

                 <div class="form-group">
                        <label>Contraseña:</label>
                        <div className="group">

                             <FontAwesomeIcon icon={faUnlock} color="#FC3955" pull="left" size="lg"  />
                             <input type="password" className="form-control" placeholder="Contraseña" required="required" />
                        </div>
                </div>
                <div className="forgot">
                    <a href="index.js">Olvidaste la contraseña?</a>
                    <p><input type="checkbox"/>Recordarme</p>
                </div>
                <button type="submit">Iniciar sesión</button>
            </div>
        </body>
    );
} 

export default Log;