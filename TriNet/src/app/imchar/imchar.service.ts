import { Injectable } from '@angular/core';

@Injectable({providedIn: "root"})
export class ImcharService {
    getPrediction() {
        return "Prediction made";
    }
}