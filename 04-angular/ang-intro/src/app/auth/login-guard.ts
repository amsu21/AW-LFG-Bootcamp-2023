import { HttpClient } from "@angular/common/http";
import { AuthService } from "./auth.service";
import { Injectable } from "@angular/core";
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from "@angular/router";
import { Observable } from "rxjs";


@Injectable({
    providedIn: 'root'
})

export class LogInGuard implements CanActivate {
    constructor(private router: Router, private authService: AuthService) {

    }

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | UrlTree | Observable<boolean | UrlTree> | Promise<boolean | UrlTree> {
        const loggedIn = this.authService.IsLoggedIn;

        if (!loggedIn) {
            this.router.navigate(['/login'])
        }
        return loggedIn;
    }
}