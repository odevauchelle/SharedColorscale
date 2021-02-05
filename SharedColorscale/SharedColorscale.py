from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from pylab import linspace

def get_cmap_range( mappables ) :

    vmin = min( [ mappable.norm.vmin for mappable in mappables ] )
    vmax = max( [ mappable.norm.vmax for mappable in mappables ] )

    return vmin, vmax

def apply_cmap_range( mappables, vmin, vmax, nb_levels = 5 ) :

    norm = Normalize( vmin, vmax )

    for mappable in mappables :
        mappable.set_norm( norm )
        mappable.changed()

    colorbar_mappable = ScalarMappable( norm = norm, cmap = mappable.cmap )
    colorbar_mappable.set_array( linspace( vmin, vmax, nb_levels + 2 )[1:-1] )

    return colorbar_mappable

def share_colorscale( mappables, nb_levels = 5 ) :
    '''
    Finds the color range of mappables, create a common colorscale and applies to corresponging plots.

    colorbar_mappable = share_colorscale( mappables, nb_levels = 5 )

    Parameters:
        mappables : a list of mappable objects (e.g. a list of contours objects)
        nb_levels [int] : number of levels in resulting colorscale

    Output:
        colorbar_mappable : the mappable object to be used with colorbar

    '''

    return apply_cmap_range( mappables, *get_cmap_range( mappables ), nb_levels = nb_levels )


#######################
#
# TRY IT OUT
#
#######################

if __name__ == '__main__' :

    from pylab import *

    x, y = meshgrid( *[ linspace( 0, 1, 30 ) ]*2 )

    figure, axs = subplots( nrows = 2, ncols = 2 )

    mappables = []

    for i, ax in enumerate( axs.flatten() ) :
        mappables += [ ax.contourf ( x, y, sin( 2*pi*2*x )*sin( 2*pi*3*y )*rand() + rand() ) ]
        ax.axis('off')

    colorbar_mappable = share_colorscale( mappables )

    colorbar( colorbar_mappable )


    show()
