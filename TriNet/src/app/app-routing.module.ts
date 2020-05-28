import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

//Imports of components
import { ImcharComponent } from './imchar/imchar.component';
import { MainComponent } from './main/main.component';
import { MnistComponent } from './mnist/mnist.component';
import { PerceptronsComponent} from './perceptrons/perceptrons.component';
import { AboutComponent} from './about/about.component';
import { TrainerComponent} from './trainer/trainer.component';
import { GridComponent } from './grid/grid.component';


//Routes for componentes
const routes: Routes = [
    { path: '', component: MainComponent },
    { path: 'imchar', component: ImcharComponent },
    { path: 'mnist', component: MnistComponent },
    { path: 'perceptrons', component: PerceptronsComponent },
    { path: 'about', component: AboutComponent },
    { path: 'grid', component: GridComponent },
    { path: 'trainer', component: TrainerComponent }
]

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}