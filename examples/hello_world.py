from pylab import meshgrid, subplots, sys, linspace, seed, rand, sin, pi, colorbar, savefig, show
sys.path.append('../SharedColorscale/')

from SharedColorscale import share_colorscale

x, y = meshgrid( *[ linspace( 0, 1, 30 ) ]*2 )

figure, axs = subplots( nrows = 2, ncols = 2 )

mappables = []

seed(1)

for i, ax in enumerate( axs.flatten() ) :

    mappables += [ ax.contourf ( x, y, sin( 2*pi*2*rand()*x )*sin( 2*pi*2*rand()*y )*(1 + rand()) + rand() ) ]
    ax.axis('off')
#
# colorbar( mappables[-1] )
# savefig( 'last_colorbar.svg', bbox_inches = 'tight' )

colorbar_mappable = share_colorscale( mappables )
colorbar( colorbar_mappable )
# savefig( 'shared_colorbar.svg', bbox_inches = 'tight' )

show()
