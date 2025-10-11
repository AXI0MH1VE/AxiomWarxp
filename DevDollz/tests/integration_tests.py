from ..devdollz_kernel.src.kernel import app

def test_home():
    with app.test_client() as client:  # type: ignore
        response = client.get('/')  # type: ignore
        assert response.data == b'DevDollz Kernel Running'  # type: ignore
