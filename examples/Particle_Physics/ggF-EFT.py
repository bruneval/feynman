import matplotlib

from feynman import Diagram

fig = matplotlib.pyplot.figure(figsize=(1.,1.))
ax = fig.add_axes([0,0,10,10], frameon=False)
diagram = Diagram(ax)
in1 = diagram.verticle(xy=(.1,.6), marker='')
in2= diagram.verticle(xy=(.1,.4), marker='')
v1 = diagram.verticle(xy=(.4,.6))
v2 = diagram.verticle(xy=(.4,.4))
v3 = diagram.verticle(xy=(.6,.5))
v4 = diagram.verticle(xy=(.34,.5), marker='')
higgsout = diagram.verticle(xy=(.9,.5))
epsilon = diagram.operator([v4,v3], c=1.1)
epsilon.text("Effective \n coupling", fontsize=30)

gluon_up_style = dict(style='linear loopy', xamp=.025, yamp=.035, nloops=7)
gluon_down_style = dict(style='linear loopy', xamp=.025, yamp=-.035, nloops=7)

g1 = diagram.line(in1, v1, **gluon_up_style)
g2 = diagram.line(in2, v2, **gluon_down_style)

higgs = diagram.line(v3, higgsout, arrow=False, style='dashed')

g1.text("g",fontsize=30)
diagram.text(v4.xy[0]-.08, v4.xy[1]-.05, "g",fontsize=35)
higgs.text("H",fontsize=30)

diagram.plot()
fig.savefig('pdf/ggF-EFT.pdf',bbox_inches='tight')
