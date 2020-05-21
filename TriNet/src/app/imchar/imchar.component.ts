import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import p5 from "p5";
import { getLocaleTimeFormat } from '@angular/common';
@Component({
    selector: 'imchar',
    templateUrl: './imchar.component.html',
    styleUrls: ['./imchar.component.css']
})
  
export class ImcharComponent implements OnInit {
    @ViewChild("canvas") public canvas: ElementRef;
    ngOnInit() {
        let sizeheight=200;
        let sizewidth=200;
        const sketch = s => {
            s.setup = () => {
                let canvas2 = s.createCanvas(400,400);
                canvas2.parent("sketch");
            };
            s.draw = () => {
                s.background(220);
                for(s.y=0; s.y<sizeheight; s.y++){
                    for(s.x=0; s.x<sizewidth; s.x++){
                        if(s.getItem(s.x+":"+s.y)==null){
                            s.storeItem(s.x +":"+ s.y, false)
                        }
                        if(s.getItem(s.x+":"+s.y)==true){
                            s.fill(0);
                        }
                        s.rect(s.x*30, s.y*30, 30, 30)
                            s.noFill();
                    }
                }
            }
            s.mouseClicked = () =>{
                for(s.y=0; s.y<sizeheight; s.y++){
                    for(s.x=0; s.x<sizewidth; s.x++){
                        if(s.mouseX < s.x*30+30 && s.mouseX > s.x*30 && s.mouseY < s.y*30+30 && s.mouseY > s.y*30){
                            s.storeItem(s.x+":"+s.y, true)
                        }
                    }
                }
            }
            s.keyTyped = () =>{
                if(s.key == " "){
                    s.clearStorage()
                }
            }
        };
        this.canvas = new p5(sketch);
    }
}