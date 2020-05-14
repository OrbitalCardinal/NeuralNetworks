import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

//Components
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { MainComponent } from './main/main.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    MainComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
