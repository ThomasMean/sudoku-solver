import pytest
import imp
gamescreen = imp.load_source("gamescreen","gamescreen.py")


def testRender():
    assert gamescreen.render(renderInput) == expectedRenderResult;

expectedRenderResult ="1|2|3|4|5|6|7|8|9\n" \
    "2|3|4|5|6|7|8|9|1\n" \
    "3|4|5|6|7|8|9|1|2\n" \
    "4|5|6|7|8|9|1|2|3\n" \
    "5|6|7|8|9|1|2|3|4\n" \
    "6|7|8|9|1|2|3|4|5\n" \
    "7|8|9|1|2|3|4|5|6\n" \
    "8|9|1|2|3|4|5|6|7\n" \
    "9|1|2|3|4|5|6|7|8"



renderInput = [[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],[4,5,6,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
