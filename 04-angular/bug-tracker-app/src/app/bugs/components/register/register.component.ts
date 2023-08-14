import { Component } from '@angular/core';
/*Import the Register service */
import { RegisterService } from './register.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  public email : string = "";
  public firstName : string = "";
  public lastName : string = "";
  public phoneNumber : string = "";
  public password : string = "";
  public passwordConfirm : string = "";
  

  
 constructor(
 private registerService : RegisterService){

  }

  
  onRegisterClick() {
    //console.log("logginh in!");
    this.registerService
      .register(this.email, this.firstName, this.lastName, this.phoneNumber, this.password)
  }
}
//emailId: string, firstName: string, lastName: string, phoneNumber: string, password: string
