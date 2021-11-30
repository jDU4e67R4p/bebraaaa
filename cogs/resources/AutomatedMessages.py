from discord import Embed
from discord import Colour

class automata:

    def generateEmbErr(x: str, error=None):
        result = Embed(
            title=f'**{x}**', color=Colour.red()
        )
        if error:
            readableErr = type(error).__name__
            result.set_footer(text=f'Error message / by Frime / {readableErr}')
        else:
            result.set_footer(text='Error message / by Frime /')
        return result

    # def generateEmbInfo(x: str):
    #     result = Embed(
    #         title=f'**{x}**',
    #         color=randCol()
    #     )
    #     result.set_footer(text='')
    #     return result