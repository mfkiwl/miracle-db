
import enum
import datetime
import gzip
import zlib
import lz4.frame
import io
import logging as log

import numpy as np

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TraceCompression(enum.Enum):
    NONE    = 1
    GZIP    = 2
    ZLIB    = 3
    LZ4     = 4

class StatTraceType(enum.Enum):
    TTRACE  = 1
    AVG     = 2
    STD     = 3
    MIN     = 4
    MAX     = 5
    RNG     = 6
    HW      = 7
    HD      = 8

class CorrolationType(enum.Enum):
    HAMMING_WEIGHT      = 1
    HAMMING_DISTANCE    = 2
    COMPLEX             = 3

def compressNDArray(traces, compression):
    """
    Returns a BytesIO object to which the traces have been written
    and compressed, ready for storage in the database
    """
    bio = io.BytesIO()

    np.save(bio, traces, allow_pickle = True)

    tr = None

    compress_begin = datetime.datetime.now()

    if(compression == TraceCompression.NONE):
        tr = bio.getvalue()

    elif(compression == TraceCompression.GZIP):
        tr = gzip.compress(bio.getvalue(), compresslevel = 9)

    elif(compression == TraceCompression.ZLIB):
        tr = zlib.compress(bio.getvalue(), level = 9)

    elif(compression == TraceCompression.LZ4):
        tr = lz4.frame.compress(
            bio.getvalue(),
            compression_level=lz4.frame.COMPRESSIONLEVEL_MAX
        )

    else:
        raise Exception("Unknown compression type: %s" % compression)

    compress_time = datetime.datetime.now() - compress_begin

    assert(isinstance(tr,bytes)),"Return value of TraceSetBlob.compress() should be of type 'bytes'"

    if(traces.nbytes < len(tr)):
        log.debug("Compression didn't save anything. Returning original data.")

        return (bio.getvalue(), TraceCompression.NONE)

    else:

        log.debug("Compressed %d bytes down to %d. Ratio = %.2fx. Took %s using %s compression." % (
            traces.nbytes, len(tr), len(tr)/traces.nbytes, compress_time,
            compression.name
        ))

    return (tr, compression)

def decompressNDArray(traces_bytes, compression):
    """
    Return an np.ndarray, which is decompressed from the supplied
    traces paramter.
    """
    assert(isinstance(traces_bytes,bytes))

    bio = None

    if(compression == TraceCompression.NONE):
        bio = io.BytesIO(traces_bytes)

    elif(compression == TraceCompression.GZIP):
        bio = io.BytesIO(gzip.decompress(traces_bytes))

    elif(compression == TraceCompression.ZLIB):
        bio = io.BytesIO(zlib.decompress(traces_bytes))
    
    elif(compression == TraceCompression.LZ4):
        bio = io.BytesIO(lz4.frame.decompress(traces_bytes))

    else:
        raise Exception("Unknown compression type: %s" % compression)
    
    return np.load(bio)

from .Device            import Device
from .Board             import Board
from .Core              import Core
from .Target            import Target
from .Experiment        import Experiment
from .TTraceSet         import TTraceSet
from .VariableValues    import VariableValues
from .TraceSetBlob      import TraceSetBlob
from .StatisticTrace    import StatisticTrace
from .CorrolationTraces import CorrolationTraces
from .ProgramBinary     import ProgramBinary

