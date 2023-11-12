---
title: Unity Development | Poem2Scene
author: Andrew-Rey
date: 2023-11-05 14:24:17
category: Project
tag:
- Unity3D
- Project
---

vr scenes generation based on poem texts.

- unity3d based
- htc vive

## framework

![1699165642361](1699165642361.png)

A simple framework of this project is shown above (maybe the *light theme* is reccomended to check the diagram). A simple idea is that the generated contents can be divided into `layer`s, and we want to controll the generation processes of layers. Such as we firstly generate `terrain` layer and define its materials and textures later in biome layer. The benefits is that the layers are generated in a more dynamic way: materials and textures are not specified in advance, but generated according to not only the texts but also the terrain layer. And so as the later layers.

## terrain

- default: noise based
- text: ai based

### noise based terrain

It is known that [Perlin noise](https://en.wikipedia.org/wiki/Perlin_noise) has a excellent perfromation in terrain/ocean wave/textures generation. And the mainly noise we used in this project is Perlin noise, but we used **2 layers**, which can simulate more abundant terrains.

The terrain layer generation parameters are shown as follow.

```csharp
// global configuration
public const           int    HeightMapRandomSeed        = 1024;
public const           int    HeightMapLength            = 256;
public static readonly int[]  HeightMapSampleFrequencies = {2, 4, 8, 16};
public const           float  HeightMapScaler            = 5f;
public const           int    TerrainLayerLength         = 512;
public const           float  TerrainLayerMaxHeight      = 1000f;
public const           string TerrainNodeName            = "TerrainNode";
public const           string TerrainLayerName           = "TerrainLayer";
```

For one noise layer case, we use simplex noise based on Perlin noise (namely overlay multiple *octaves* on the base noise). The result is show in the image.

![one-layer noise](image.png)

We can see the result is realisitic in a way. However, the problem is that, there are less reasonable places the our world. This generated scene is more "noise", but our world has more terrain types such as "plane". So we designed a two-layer noises to generate terrain and it has a more reasonable result. Here is the image.

![two-layer noise](1699168066108.png)

For two-layer case, we controll the amplitudes of the "mountains" using a strategy (by default, we use 1-frequency and 1-octave Perlin noise). And the variance of terrain is more smooth and more "not random".

## schedule/progress

**23-11-07**
target:

- add start ui (simple version: v_1)
  - [learn the vr ui](https://learn.unity.com/tutorial/creating-a-vr-menu-2019-2?uv=2019.4#)
  - use button-click to change scene (from start-scene to main-scene)
- realize terrain real-time loading
  - define chunks
  - generate base map (defaultly include 16 by 16 chunks)
  - load chunk around the player (load 9 chunks and player is in the center chunk)
    - check per-frame
  - finish `MapLoader`
  - finish `BaseMap`
  - modified the map generation steps
    - when firstly load the game, generate whole resources used in the map (height gradient meshes, amplitude gradient mesh, biome, decorations, ...), store them to resource file (why do we use this method -- dynamic loading and promising the continuity between chunks)
    - generate chunks around the player, based on the gradient data
    - if enter a brand new area, load the gradient data and generate chunks

**23-11-08**
target:

- continue to complete the `MapLoader` and `BaseMap`
  - generate `BaseMap` and divide it into chunks
  - store data into files
- clear up thinking
  - base-map has the total attributes of map, including terrain, biome, building and weather properties
  - for the generation of base-map: just generate the related data and store them into files
  - base-map-loader is used to load data and generate details of maps around the player
  - every chunk is a smaller map, which means base-map is a data-struct
  - chunk is also a game object, the parents node of terrain and the decorations on it

**23-11-10**
target:

- rewrite `TerrainLayer` and `TerrainNode` and `HeightMap`
  - support *chunk-like* terrains
  - provide more interfaces *to get the middle result or data*
- the whole project is ready to be in a mass...
  - arrange project structure