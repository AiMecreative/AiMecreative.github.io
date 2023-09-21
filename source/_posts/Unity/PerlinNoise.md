---
title: 【PCG】Perlin Noise
date: 2023-09-21 00:25:23
tags:
- Unity
- PCG
- Terrain
category: Unity
Author: AndrewRey
---
“程序化内容生成——地形/材质等的程序化生成”

——关于一些剑走偏锋的项目历程

<!--more-->

### Perlin Noise

> about the Perlin noise: [ref](https://rtouti.github.io/graphics/perlin-noise-algorithm)

> 4 types of noise that are similar and that are often confused with one another
>
> - classic Perlin noise
> - improved Perlin noise
> - simplex noise
> - valuse noise

> about the range of Perlin noise: [ref](https://digitalfreepen.com/2017/06/20/range-perlin-noise.html)

```csharp
// mapping a 2D position to a random number range from -1 to 1
var perlinValue = PerlinNoise(float x, float y);
```

> for texture: x, y stand for pixel position, but multiplied by a small number called the frequency

- **Parameters**
  - frequency of 2D waves
  - amplitude of 2D waves
  - octaves: the amount of waves to be generated
  - persistence: amount of change in size between one curve and the next
  - offset: provide variation in the output
  - height scale: scaling factor to accentuate the output generated

> **Property**
> if 2 inputs are near to each other, the results of the noise function will be near to each other too.
>
> - guarantee continuity

#### Generation

- given a 2D grid as following, the input of Perlin noise is each pixel.

![1695262810353](1695262810353.png)

- assign each gird point a random constant vector. (note: gridVector[4])
- get the vectors pointing from the grid point to the input point(target pixel). (note: inputVector[4])
- for each of the 4 corners of the square where the target pixel lies, calculate the dot products: for i in range(4): calculate dot(gridVector[i], inputVector[i])

![1695264135606](1695264135606.png)

- interpolate between those 4 values and the result is the value of the target pixel.

> difference between Perlin noise and value noise:
> Perlin noise use **dot product** between 2 vectors to get 4 corners' values while value noise use a pseudo-random number.

#### Discussion

> **gradient constant vectors**
> 
> - **why we need permutation table(noted as `P`) & gradient table(noted as `G`)**: P is used to *select* a random gradient from G. P provides randomness and repeatability(???)4
>
> - **how to generate a permutation table**: the core is *double* and *shuffle*. we have known that permutation table is used to select a gradient from gradient table and one gradient is defined by (x,y) (which is the grid point position). so one tuple (x,y) defines one permutation value. so the size of permutation table is $len(X)\times len(Y)$ (*double*). to guarantee the randomness, we can do shuffle for $0-255$. the code to generate permutation table is (where $len(X) = len(Y)$):
> 
> ```csharp
> var permutationTable = new int[2 * len(X)];
> for (var i = 0; i < len(X); i += 1) permutationTable[i] = i;
> permutationTable = Shuffle(permutationTable);
> for (var i = 0; i < len(X); i += 1) permutationTable[len(X) + i] = permutationTable[i];
> // visit the table given (x,y)
> var valueTopRight = P[P[x+1]+y+1];
> var valueTopLeft = P[P[x]+y+1];
> var valueBottomRight = P[P[x+1]+y];
> var valueBottomLeft = P[P[x]+y];
> ```
>
> - **how to generate a gradient table**: use 4 constant vectors: $(1f,1f), (1f, -1f), (-1f, 1f), (-1f, -1f)$. so just do modulo with the permutation value given (x,y) can get one gradient vector.
>
> ```csharp
> Vector2 GetConstantVector(v) {
>   switch v % 4:
>     case 0: return Vector2(1f,1f);
>     case 1: return Vector2(1f,-1f);
>     case 2: return Vector2(-1f,1f);
>     case 3: return Vector2(-1f,-1f);
>     default: throw undefined error;
> }
> ```
