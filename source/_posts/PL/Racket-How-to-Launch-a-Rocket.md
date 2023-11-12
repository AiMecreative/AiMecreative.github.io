---
title: Racket | How to launch a rocket
author: Andrew-Rey
date: 2023-11-11 20:55:57
category: Programming Language
tag:
- Racket
- Functional Programming
---

"...Introductory books on programming tend to contain lots of materials about the authors' favorate application discipline: puzzles, mathematics, physics, music and so on. **Such material is natural because programming is obviously useful in all these areas, but it also dstracts from the essential elements of programming.** Hence, we have made every attempt to minimize the use of knowledge from other areas so that **we can focus on what computer science can teach you about computational problems solving.**"

<!--more-->

### show an image

Zerothly, you want to show your favorate image on the screen, such as the rocket.

Firstly, maybe you in your DrRacket but I used to use my VSCode anyway, if you want to show an image, one convinient module is `slideshow`, just add `#lang slideshow` in the first line.

Secondly, just look up the help manual and find a function called `show-pict`, which can display and image. Meanwhile, `bitmap/file` can load an image based on the given string-like path. So just use as what I did:

```racket
#lang slideshow
(show-pict (bitmap/file "path/to/image"))
```

Run and you will see:

![1699773585285](1699773585285.png)

Yes, and we will **launch** it into the sky.

### define a scene

Racket provides an empty-scene where we can put our objects on it (of course, out of it is just ok), use `empty-scene` to define.
Now we put our samll rocket `overlay` it but with a smaller size using `scale`. Before that, you should `(require 2htdp/image)` to add package.

```racket
(require 2htdp/image)
(empty-scene 800 600)
(overlay (scale 0.2 (bitmap/file "path/to/image")) scene)
```

But this expression maybe a little annoyed as the nested and confused expressions. So it's necessary to `define` some constants and variables.

```racket
; constants
(define image-scaler .2)
(define scene-length 800)
(define scene-width 600)
(define x-offset 0)
(define max-height (/ scene-width 2))
(define min-height (- 0 (/ scene-width 2)))

; variables
(define scene (empty-scene scene-length scene-width))
(define rocket (scale image-scaler (bitmap/file "path/to/image")))

; interactions
(show-pict (overlay rocket scene))
```

![1699774549772](1699774549772.png)

> **Note**: the CENTER coordinate is (0, 0)

### change positions

We use `overlay/offset` to define the relative position on our scene. Insert a xy-pair between `rocket` and `scene` to define the rocket's position on scene. If we want show another little different positions, just modify the xy-pair to another values.

There we use a function provided by `2htdp/universe` named `animate`, which consumes *a function as an variable* and apply it to time tick every frame. 

Inaddition, we prefer to use `function` to do such work.

```racket
; functions
(animate (λ (height) 
  (overlay/offset rocket x-offset height scene)))
```

![1699775538374](1699775538374.gif)

### refine the program

Anyway, the rocket can fly *safely?* But there is a little more problems in our program.

- the rocket flies out of our scene, should stop when flies too high
- the rocket flies with a constant speed, should be accelerated
- the rocket flies start on the scene center, not the land

```racket
; add acceleration in our rocket
(define acceleration .5)
(define (get-height t)
  (/ (* acceleration (* t t)) 2))

; stop when reach to the highest use max or min height defined above
(define (get-location t)
  (min (+ min-height (get-height t)) max-height))

; the finally animation
(define (fly-up t)
  (overlay/offset rocket x-offset (get-location t) scene))
```

![1699776100626](1699776100626.gif)

> although you can launch a rocket in some degrees, but however, you learnt nothing. I mean you are just coding but with an image or with a new programming language. The same problems appear when you construct a larger project in your usual life. We not learn functional programming but learn the essential elements of programming, learn the construction of projects and learn how to use these tools to solve computational problems.
