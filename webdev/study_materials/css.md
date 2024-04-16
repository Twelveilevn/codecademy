# *SYNTAX AND SELECTORS*
```HTML
<head>
    <link href="style.css" rel="stylesheet">
</head>
```
### Selectors
```CSS
p {
    color: blue; /*property and value*/
}

* { /*universal selector*/
    ...;
}

.classname { /*class selector*/
    ...;
}

#idname { /*id selector*/
    ...;
}

[href] { /*attribute selector*/
    ...;
}

img[src="winter"] {
    ...;
}
```

```CSS
<h1 class="green bold">...</h1>
/*multiple classes*/
/*classes are meant to be used over many elements*/
.green {
    ...;
}
.bold {
    ...;
}
```
# *VISUAL RULES*
# *BOX MODEL*
# *DISPLAY AND POSITIONING*
# *COLORS*
# *TYPOGRAPHY* 
# *FLEXBOX*
# *GRID*
## Grid template areas
- allows you to name sections of the web page to use as values in the `grid-row-start`, `grid-row-end`, `grid-column-start`, `grid-column-end`, `grid-area`
```CSS
grid-template-areas: "header header"
                     "nav nav"
                     "info services"
                     "footer footer"

header {
    grid-area: header;
}

nav {
    grid-area: nav;
}

.info {
    grid-area: info;
}
```
- creates a 2 column, 4 row layout and assigns elements to it
## Overlapping elements
- can be solved by using the `z-index` 
## Justify items
ROW - inline axis
COLUMN - block axis
`justify-items: ;`(`start`, `end`, `center`, `stretch`)
- declared on grid containers and positions the items along the inline axis
## Justify content
- declared on grid containers and allows to adjust the position of the grid itself
`justify-content: ;`(`start`, `end`, `center`, `stretch`, `space-around`, `space-between`, `space-evenly`)
## Align items
- positioning grid items on the vertical axis
`align-items: ;`(`start`, `end`, `center`, `stretch`)
## Align content
- declared on grid containers and positions the rows on the vertical axis
`align-items: ;`(`start`, `end`, `center`, `stretch`, `space-around`, `space between`, `space-evenly`)
## Justify self nad Align self
- declared on grid items 
`justify-self: ;`(`start`, `end`, `center`, `stretch`)
`align-self: ;`(`start`, `end`, `center`, `stretch`)
## Grid auto rows and Grid auto columns
- declared on grid containers when we dont know the exact amount of grid items. If there are more grid items than grid spaces, the items overflow and automatically resize
`grid-auto-rows: ;`
`grid-auto-columns: ;`
## Grid auto flow
- declared on grid containers and specifies wheather new element should be added to rows or columns
`grid-auto-rows: ;`(`row`, `column`, `dense`)
# *TRANSITIONS*
## Duration
- to create a transition we must specify property that we want to transition and duration of the transformation
```CSS
a {
  transition-property: color; (color, background-color font-size, width, height)
  transition-duration: 1s;
}
```
## Timing function
`transition-timing-function: ;`(`ease-in`, `ease-out`, `ease-in-out`, `linear`)
## Delay
`transition-delay: 0.5s;`
## Transition
`transition: transition-property transition-duration transition-timing-function transition-delay;`
## Combinations
- combining transitions with `,`
```CSS
transition: color 1s linear, font-size 750ms ease-in 100ms;

transition: all 1s linear 0.2s; /*applies the same effects to all elements*/
```