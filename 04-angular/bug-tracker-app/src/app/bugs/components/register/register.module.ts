import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { CommonModule } from '@angular/common';
import { RegisterComponent } from './register.component';

import { RegisterRoutingModule } from './register-router.module';
import { RegisterService } from './register.service';



@NgModule({
  declarations: [
    RegisterComponent,
 
  ],
  providers : [
    RegisterService
  ],
  imports: [
    CommonModule,
    HttpClientModule,
   RegisterRoutingModule
  ],
  exports : [
    RegisterComponent
  ]
})
export class RegisterModule { }
