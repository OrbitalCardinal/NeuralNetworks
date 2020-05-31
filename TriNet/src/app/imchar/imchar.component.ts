import { Component, OnInit, ViewChild, ElementRef, Input, Output } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import p5 from "p5";
@Component({
    selector: 'imchar',
    templateUrl: './imchar.component.html',
    styleUrls: ['./imchar.component.css']
})
  
export class ImcharComponent implements OnInit{
    constructor(private http: HttpClient) {}
    myp5: any;
    ngOnInit() { 
        let sketch = function(p) {
            p.output = [];
            p.n = 9;
            var pixelArray = [];
            var w = 400;
            var h = 400;
            var rows = w/p.n;
            var columns = h/p.n;
            p.setup = function() {                
                let canvas2 = p.createCanvas(w,h);
                canvas2.parent("grid");
                //Pixel array
                for(var i=0; i<p.n; i++) {
                    for(var j=0; j<p.n; j++) {
                        var xpos = j * rows;
                        var ypos = i * columns;
                        pixelArray.push(new Pixel(xpos,ypos,rows,columns));
                    }
                }              
            }
            
            p.draw = function() {
                p.background(0);
                for(var i=0; i<pixelArray.length; i++) {
                    pixelArray[i].show();
                    if(p.mouseIsPressed) {
                        for(var j=0; j<pixelArray.length; j++) {
                            pixelArray[j].clicked(p.mouseX, p.mouseY, i);
                        }
                    }
                }
            }
            
            p.reset = function() {
                for(var i=0; i<pixelArray.length; i++) {
                    pixelArray[i].color = 0;
                    pixelArray[i].value = -1;
                }
            }
            
            p.predict = function() {
                p.output = [];
                for(var i=0; i<pixelArray.length; i++) {
                    p.output.push(pixelArray[i].value);
                }
            }
            
            class Pixel {
                x1: number;
                y1: number;
                x2: number;
                y2: number;
                color: number;
                value: number;
                
                constructor(x1: number, y1: number, x2: number, y2: number) {
                    this.x1 = x1;
                    this.y1 = y1;
                    this.x2 = x2;
                    this.y2 = y2;
                    this.color = 0;
                    this.value = -1;
                }
                
                clicked(x: number, y: number) {
                    if(x > this.x1 && x < this.x1+rows && y > this.y1 && y < this.y1+columns) {
                        this.color = 255;
                        this.value = 1;
                    } else {
                        if(this.color != 255) {
                            this.color = 0;
                        }
                    }
                }
                
                show() {
                    p.stroke(50);
                    p.fill(this.color);
                    p.rect(this.x1,this.y1,this.x2,this.y2);
                }
            }
        }
        this.myp5 = new p5(sketch);
    }
    
    // prediction: string;
    // @Input() output: number[];
    prediction: any;
    getPrediction() {
        this.myp5.predict();
        var outputString = "";
        var n = this.myp5.output.length
        for(var i=0; i<n; i++) {
            if(i == n-1) {
                outputString += this.myp5.output[i].toString();
            } else {
                outputString += this.myp5.output[i].toString() + " ";
            }
        }
        
        var outputJson = {
            data: outputString,
            dimension: this.myp5.n
        }
        this.http.post<{data: string, dimension: number}>("http://localhost:3000/api/imchar", outputJson)
        .subscribe(response => {
            this.prediction = response.data
        });
        // this.http.get<{message: string}>("http://localhost:3000/api/imchar")
        // .subscribe((data) => {
        //     this.prediction = data.message;
        // });
    }
    
    reset() {
        this.myp5.reset()
        this.prediction = "";
    }
}