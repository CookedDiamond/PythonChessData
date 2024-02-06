import plotter
import onlinegame



og = onlinegame.Request("cookeddiamond")
res = og.getSignleGame("100897403067")
print("Got single game")

p = plotter.Plotter()
p.readGame(res)
p.calcBlunders()
p.openPlot()

print(res)
