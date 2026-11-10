# balli baan

A little browser game: build a marble run in a sandbox (*zandbak*) with your hands, then let the ball roll.

Open `index.html` in a browser (it loads three.js from cdnjs). No build step.

## Hands

| Key | Hand   | What it does |
|-----|--------|--------------|
| 1   | Dig    | Scoops sand away and pushes it up into banks beside your stroke. |
| 2   | Pile   | Drops sand to build walls and hills. |
| 3   | Smooth | Pats the sand flat. |
| 4   | Tunnel | One finger carves a track that never climbs. Where the sand is deep enough it goes underground. |

Right-drag (or two fingers) turns the camera, scroll or pinch zooms, space rolls the ball, Ctrl+Z undoes a stroke.

## Sandboxes

1. **First run**: dig a runway from the pipe to the cup.
2. **The dune**: tunnel through a dune.
3. **Rock garden**: rocks can't be moved, so wind around them.
4. **Free play**.

Reaching the cup earns one star; each shell the ball rolls over earns another.

## How it works

The sand is two heightfields on a 128×128 grid: `ground` (what the ball rolls on) and `top` (the visible surface).
Where `top` is above `ground` there is a tunnel, and the roof mesh is cut open at the tunnel mouths.
Sand slumps to a maximum slope after every stroke. The ball is a sphere colliding with the heightfield
(nine contact samples per sub-step, 2 ms sub-steps) with rolling friction and a ceiling inside tunnels.
