import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

//Imports of components
import { ImcharComponent } from './imchar/imchar.component';
import { MainComponent } from './main/main.component';

//Routes for componentes
const routes: Routes = [
    { path: '', component: MainComponent },
    { path: 'imchar', component: ImcharComponent}
]

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}