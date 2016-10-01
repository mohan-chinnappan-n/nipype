# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import Smooth


def test_Smooth_inputs():
    input_map = dict(data_type=dict(field='dtype',
    ),
    fwhm=dict(field='fwhm',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    implicit_masking=dict(field='im',
    ),
    in_files=dict(copyfile=False,
    field='data',
    mandatory=True,
    ),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    out_prefix=dict(field='prefix',
    usedefault=True,
    ),
    paths=dict(),
    use_mcr=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    )
    inputs = Smooth.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Smooth_outputs():
    output_map = dict(smoothed_files=dict(),
    )
    outputs = Smooth.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value