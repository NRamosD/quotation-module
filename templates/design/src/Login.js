import React, {Component} from 'react';
import './css/style.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUnlock, faUser } from '@fortawesome/free-solid-svg-icons'
 


class Log extends Component{

    state = {
        credentials:{
            user:"",
            pass:""
        }
    }
    login = e =>{
        console.log(this.state.credentials)
        fetch('',{
            method: '',
            headers: '',
            body: ''
        })

    }

    inputChanged = e =>{
        const crd = this.state.credentials;
        crd[e.target.name]=e.target.value;
        this.setState({credentials: crd});
    }


    render(){
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
                                <input name="user" type="text" className="form-control" 
                                placeholder="Nombre de usuario" required="required" 
                                value={this.state.credentials.user} onChange={this.inputChanged}/>
                            </div>
                        </div>
                    </form>

                    <div class="form-group">
                            <label>Contraseña:</label>
                            <div className="group">

                                <FontAwesomeIcon icon={faUnlock} color="#FC3955" pull="left" size="lg"  />
                                <input name="pass" type="password" className="form-control" 
                                placeholder="Contraseña" required="required" 
                                value={this.state.credentials.pass} onChange={this.inputChanged}/>
                            </div>
                    </div>
                    <div className="forgot">
                        <a href="index.js">Olvidaste la contraseña?</a>
                        <p><input type="checkbox"/>Recordarme</p>
                    </div>
                    <button type="submit" onClick={this.login}>Iniciar sesión</button>
                </div>
            </body>
        );
    }
} 

export default Log;