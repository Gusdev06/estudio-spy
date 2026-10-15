# Segmentação de pessoa (MediaPipe selfie_multiclass) — roda no venv com mediapipe (scratchpad segenv). Retorna máscara float 0-1 por frame.
import mediapipe as mp, numpy as np, cv2, os
from mediapipe.tasks.python import vision, BaseOptions
MOD=os.environ.get('SEGMOD','/private/tmp/claude-501/-Users-gustagoat-Documents-AIS-OS/2e06f3b3-83c2-4c3f-90b2-f601cf26c41e/scratchpad/selfie_multiclass.tflite')
_seg=None
def seg(bgr):
    global _seg
    if _seg is None:
        _seg=vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(base_options=BaseOptions(model_asset_path=MOD),output_confidence_masks=True,output_category_mask=False))
    im=mp.Image(image_format=mp.ImageFormat.SRGB,data=np.ascontiguousarray(cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)))
    cm=_seg.segment(im).confidence_masks
    bg=cm[0].numpy_view().copy()
    parts={k:cm[i].numpy_view().copy() for i,k in enumerate(['bg','hair','body','face','clothes','other'])}
    return (1-bg).reshape(bg.shape[:2]), {k:v.reshape(bg.shape[:2]) for k,v in parts.items()}
