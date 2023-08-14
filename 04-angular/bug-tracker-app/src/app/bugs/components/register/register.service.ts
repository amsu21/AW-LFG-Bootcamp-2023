import { Injectable } from "@angular/core";
import { RegisterRequest, RegisterResponse, User} from "./register.model";
import { HttpClient } from "@angular/common/http";

@Injectable({
    providedIn : 'root'
})
export class RegisterService {
    private _isLoggedIn : boolean = false;
    private _currentUser!: User;
    private _accessToken : string = '';

    constructor(private httpClient : HttpClient){

    }
    get IsLoggedIn() : boolean {
        return this._isLoggedIn;
    }

    get CurrentUser() : User {
        return this._currentUser;
    }

    get AccessToken() : string {
        return this._accessToken;
    }

    register(email: string, firstName: string, lastName: string, phoneNumber: string, password: string) {
        const registerRequest : RegisterRequest = {
            email : email,//<model>: <html bind>
            password : password,
            firstName: firstName,
            lastName: lastName,
            phoneNumber: phoneNumber
        }
        this.httpClient
            .post<RegisterResponse>('http://localhost:3000/register', registerRequest)
            .subscribe(res => {
                this._isLoggedIn = true;
                this._currentUser = res.user;
                this._accessToken = res.accessToken;
            })
    }

    logout() {
        this._accessToken = '';
        this._isLoggedIn = false;
        
    }
}