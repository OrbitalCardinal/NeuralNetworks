import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from "@angular/common/http";
@Component({
    selector: 'imchar',
    templateUrl: './imchar.component.html',
    styleUrls: ['./imchar.component.css']
})
  
export class ImcharComponent {
    
    constructor(private http: HttpClient) {}
    
    prediction: string;
    
    getPrediction() {
        this.http.get<{message: string}>("http://localhost:3000/api/imchar")
        .subscribe((data) => {
            this.prediction = data.message;
        });
    }
}