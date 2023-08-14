import { Component } from "@angular/core";
import { AuthService } from "./auth.service";

@Component({
    selector: 'app-login',
    templateUrl: 'login.component.html',
    styleUrls: ['login.component.css']
})

export class LoginComponent {
    emailId : string = '';
    password : string = '';

    constructor(public authService : AuthService) {

    }

    onBtnLoginClick() {
        this.authService
            .login(this.emailId, this.password)
    }
}