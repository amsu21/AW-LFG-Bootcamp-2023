import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

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
    ShoppingCartComponent

  ],
  /* All the dependency modules  */
  imports: [
    BrowserModule
  ],
  /* All the NON-UI entities (services) */
  providers: [
    // SalaryCalculatorModel
    { provide : SalaryCalculatorModel, useClass : SalaryCalculatorModel },
    // { provide :SalaryCalculatorModel, useClass : SalaryCalculatorModelV2 }
    ProductsService
  ],

  /* top level components */
  bootstrap: [AppComponent]
})
export class AppModule { }
