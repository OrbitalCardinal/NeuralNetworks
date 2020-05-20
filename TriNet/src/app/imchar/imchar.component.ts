import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import p5 from "p5";
@Component({
    selector: 'imchar',
    templateUrl: './imchar.component.html',
    styleUrls: ['./imchar.component.css']
})
  
export class ImcharComponent implements OnInit {
    @ViewChild("canvas") public canvas: ElementRef;
    ngOnInit() {
        const sketch = s => {
            s.setup = () => {
                let canvas2 = s.createCanvas(200,200);
                canvas2.parent("sketch");
                s.background(0);
            };
            s.draw = () => {
                
            };
        };
        this.canvas = new p5(sketch);
    }
}