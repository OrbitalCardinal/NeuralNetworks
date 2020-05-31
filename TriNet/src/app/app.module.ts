import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpErrorResponse } from "@angular/common/http";
import { FormsModule} from '@angular/forms';

//Components
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ImcharComponent } from './imchar/imchar.component';
import { AppRoutingModule } from './app-routing.module';
import { MainComponent } from './main/main.component';
import { MnistComponent } from './mnist/mnist.component';
import { PerceptronsComponent} from './perceptrons/perceptrons.component';
import { AboutComponent} from './about/about.component';
import { TrainerComponent } from './trainer/trainer.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    ImcharComponent,
    MainComponent,
    MnistComponent,
    PerceptronsComponent,
    AboutComponent,
    TrainerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
