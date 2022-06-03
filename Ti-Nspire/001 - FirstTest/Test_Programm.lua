-- Get the screen
local screen = platform.window
local h = screen:height()
local w = screen:width()
local text = "Test"

-- Drawing an text
function on.paint(gc)
    local sw = gc:getStringWidth(text)
    local sh = gc:getStringHeight(text)

    gc:setFont("sansserif", "b", 12)
    gc:setColorRGB(158, 5, 8)
    gc:drawString("Test", w/2 - sw/2, 0)
end