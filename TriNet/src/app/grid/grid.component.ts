import { OnInit, Component,ViewChild, ElementRef } from '@angular/core';
import p5 from "p5";
@Component({
    selector: 'grid',
    templateUrl: './grid.component.html',
    styleUrls: ['./grid.component.css']
})
export class GridComponent implements OnInit {
    @ViewChild("canvas") public canvas: ElementRef;
    ngOnInit() { 
        let sketch = function(p) {
            var n = 16;
            var pixelArray = [];
            var w = 400;
            var h = 400;
            var rows = w/n;
            var columns = h/n;
            
            p.setup = function() {
                p.frameRate(60);
                let canvas2 = p.createCanvas(w,h);
                canvas2.parent("grid");
                p.resetSketch();
                var button = p.createButton("reset");
                button.mousePressed(p.resetSketch);
            }
            p.resetSketch = function(){
                for(var i=0; i<n; i++) {
                    for(var j=0; j<n; j++) {
                        var xpos = i * rows;
                        var ypos = j * columns;
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
                            pixelArray[j].clicked(p.mouseX, p.mouseY);
                        }
                    }
                }
            }

          
        
            
            class Pixel {
                x1: number;
                y1: number;
                x2: number;
                y2: number;
                color: number;
                
                constructor(x1: number, y1: number, x2: number, y2: number) {
                    this.x1 = x1;
                    this.y1 = y1;
                    this.x2 = x2;
                    this.y2 = y2;
                    this.color = 0;
                }
                
                clicked(x: number, y: number) {
                    if(x > this.x1 && x < this.x1+rows && y > this.y1 && y < this.y1+columns) {
                        this.color = 255;
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
        this.canvas = new p5(sketch);
    }
}