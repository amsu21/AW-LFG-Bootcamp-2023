import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

//for server communication using "HttpClient" service
import { HTTP_INTERCEPTORS, HttpClientModule } from "@angular/common/http";

/* for implementing the routing capabilities */
import { RouterModule, Routes } from "@angular/router";

import { AppComponent } from './app.component';
import { GreeterComponent } from "./greeter/greeter.component";
import { CalculatorComponent } from './calculator/calculator.component';
import { Calculator2Component } from './calcultor-2/calculator2.component';
import { ProductsComponent } from './products/products.component';
import { SalaryCalculatorComponent } from './salary-calculator/salary-calculator.component';
import { SalaryCalculatorModel } from './salary-calculator/models/salary-calculator.model';
import { SalaryCalculatorModelV2 } from './salary-calculator/models/salary-calculatorV2.model';
import { CalculatorResultComponent } from './calculator-result/calculator-result.component';
import { SalaryCalculatorResultComponent } from './salary-calculator/salary-calculator-result/salary-calculator-result.component';
import { ComponentParent } from './comp-comm/comp-parent.component';
import { ComponentChild } from './comp-comm/comp-child.component';
import { ShoppingCartComponent } from './shopping-cart/shopping-cart.component';
import { ProductsService } from './shopping-cart/services/products.service';
import { CartService } from './shopping-cart/services/cart.service';
import { CartStatsComponent } from './shopping-cart/components/cart-stats/cart-stats.component';
import { BugsComponent } from './bugs/bugs.component';
import { PathNotFoundCompnent } from './path-not-found.component';
import { HomeComponent } from './home.component';
import { LoginComponent } from './auth/login.component';
import { LogInGuard } from './auth/login-guard';
import { HttpLogInterceptor } from "./utils/httpLoginterceptor";
import { HttpAuthorizeInterceptor } from "./utils/httpAuthorizeInterceptor";

/* define the routes */
const routes : Routes = [
  { path: "", component: HomeComponent },
  { path : "login", component : LoginComponent},
  { path: "greeter", component : GreeterComponent, canActivate : [LogInGuard] /* canActivate guard is used to check if the route can be activated */},
  { path: "calculator", component: CalculatorComponent , canActivate : [LogInGuard]},
  { path: "calculator-2", component: Calculator2Component , canActivate : [LogInGuard]},
  { path: "salary-calculator", component: SalaryCalculatorComponent , canActivate : [LogInGuard]},
  { path: "bugs", component: BugsComponent, canActivate: [LogInGuard] },
  /* { path: "**", component: PathNotFoundCompnent } */
  {path : "**", redirectTo : ""}
]

export const httpInterceptorProviders = [
  { provide: HTTP_INTERCEPTORS, useClass: HttpLogInterceptor, multi: true },
  { provide: HTTP_INTERCEPTORS, useClass: HttpAuthorizeInterceptor, multi: true },
];

@NgModule({
  /* All the UI entities (component, directive, pipe) */
  declarations: [
    AppComponent,
    GreeterComponent,
    CalculatorComponent,
    Calculator2Component,
    ProductsComponent,
    SalaryCalculatorComponent,
    CalculatorResultComponent,
    SalaryCalculatorResultComponent,
    ComponentParent,
    ComponentChild,
    ShoppingCartComponent,
    CartStatsComponent,
    BugsComponent,
    PathNotFoundCompnent,
    HomeComponent,
    LoginComponent
  ],
  /* All the dependency modules  */
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  /* All the NON-UI entities (services) */
  providers: [
    // SalaryCalculatorModel
    { provide : SalaryCalculatorModel, useClass : SalaryCalculatorModel },
    // { provide :SalaryCalculatorModel, useClass : SalaryCalculatorModelV2 }
    ProductsService,
    CartService,
    // register the http interceptors
    httpInterceptorProviders
  ],

  /* top level components */
  bootstrap: [AppComponent]
})
export class AppModule { }
