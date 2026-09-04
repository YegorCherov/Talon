# Talon

Talon is a single motor ducted drone that uses thrust vectoring for flight control.

<table>
<tr>
<td><img src="images/Isometric.png" alt="Isometric View" width="400" /></td>
<td><img src="images/Top.png" alt="Top View" width="400" /></td>
</tr>
</table>

## CAD and Hardware Layout

<img src="images/Isometric.png" alt="Isometric View" width="450" />

The isometric view shows how the main parts package together. The motor and three blade propeller sit on the center top plate. Four micro servos sit around that middle ring, each hooked directly to one of the rectangular control vanes below. The duct wraps around the prop, with a raised lip on the cowl to help guide airflow into the blades.

<img src="images/Top.png" alt="Top View" width="450" />

Looking down into the duct shows the propeller sitting over eight curved stator vanes. Those stators connect the center motor mount to the outer ring. Their curve is shaped to catch the spinning air coming off the prop and straighten it out to cancel motor torque. Underneath the stators, the four control vanes sit at ninety degree intervals.

<img src="images/Front.png" alt="Side View" width="450" />

The side view shows the vertical layout. The white cylinder at the bottom houses the 4S battery, keeping the heaviest part of the build down low and centered directly under the thrust line. On the cowl, there are cutouts for the USB port and status LED so you can plug into the flight controller without taking the duct apart.

<img src="images/Bottom.png" alt="Bottom View" width="450" />

The bottom view shows the exhaust path. The four control vanes sit directly in the fastest air stream coming out of the duct. Each vane pivots on its own axis to deflect air for pitch, roll, and yaw. You can also see the wire routing holes and mounting points for the internal electronics plate.

## How It Works

A single brushless motor and three blade propeller sit at the top of the duct.

Because a single prop creates rotational torque, eight curved stator vanes sit inside the duct to straighten the airflow and cancel out motor torque passively.

Directly below the stators, four control vanes are connected to micro servos positioned at ninety degree intervals. Deflecting opposing pairs controls pitch and roll. Deflecting all four vanes together controls yaw and trims out any remaining motor torque.

The lower cylinder holds the battery to keep the heaviest component low and centered directly under the thrust axis.

## Measured Data and Specs

| Parameter | Value |
|---|---|
| Total flying weight | 550 g |
| Battery weight | 217 g (4S pack) |
| Airframe and electronics | 330 g |
| Expected thrust | 850 g to 1190 g |
| Thrust to weight ratio | 1.55 to 2.17 |

## Mechanical and Control Notes

Control authority depends directly on prop wash speed. When throttle is low, the vanes have less air passing over them and react slower.

The curved stator vanes handle the bulk of the motor torque during hover, leaving the four servo vanes to focus on attitude control and fine yaw adjustments.

Linkages between the servos and control vanes need to be stiff to avoid flutter at full throttle.

## Bill of Materials

| Part | Qty | Cost (est.) | Link |
|---|---|---|---|
| Motor (2810 1350KV) | 1 | $5.33 | link |
| 8" propeller | 4 | $3.4 | link |
| Micro servo (control vanes) | 4 | $0.5 each ($2 total) | link |
| ESC (40A) | 1 | $5.33 | link |
| Flight controller | 1 | $4-10 | link |
| Camera | 1 | $6.70 | link |
| Radio | 1 | $5.30 | link |
| 4S LiPo battery | 1 | $13.4 | link |
| M2 / M3 screws | assorted | $2 | link |
| PETG/PLA filament | ~300g | $3-4 | link |
| **Total** | | **~$50-57** | |

## Repo Structure

```
3d print/     Printable parts
cad/
  v1/
  v2/
  v3-final/   current
images/
```

## Status

Mechanical layout is settled, nothing's flight tested yet. Check CHANGELOG.md for what changed between versions.

## License

MIT. Use it, change it, fly it, just don't blame me if it doesn't.
