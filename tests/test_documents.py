import pytest
import httpx
from fastapi import status


HOST = 'http://127.0.0.1:5000'
SAMPLE_LARGE_TEXT = (
    "The black currawong (Strepera fuliginosa), also known as the black jay, is a large passerine bird endemic to "
    "Tasmania and nearby islands in the Bass Strait. One of three currawong species, it is closely related to the "
    "butcherbirds and Australian magpie in the family Artamidae. It is a large crow-like bird, around 50 cm (20 in) "
    "long, with yellow irises, a heavy bill, and black plumage with white wing patches. The sexes are similar in "
    "appearance. Three subspecies are recognised, one of which, S. f. colei of King Island, is vulnerable to "
    "extinction. The black currawong is generally sedentary, although populations at higher altitudes relocate to "
    "lower areas during the cooler months. The habitat includes densely forested areas as well as alpine heathland. It "
    "is rare below altitudes of 200 m (660 ft). Its omnivore diet includes a variety of berries, invertebrates, and "
    "small vertebrates. Less arboreal than the pied currawong, the black currawong spends more time foraging on the "
    "ground. It roosts and breeds in trees."
)

SAMPLE_SHORT_TEXT = "This is a very short text."


@pytest.mark.asyncio
class TestRoutes:
    async def test_routes_exist(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(HOST + "/documents/")
            assert response.status_code not in (
                status.HTTP_404_NOT_FOUND,
                status.HTTP_405_METHOD_NOT_ALLOWED,
            )


@pytest.mark.asyncio
class TestDocuments:

    async def test_create_document(self):
        async with httpx.AsyncClient() as client:
            form = {"text": SAMPLE_LARGE_TEXT}
            response = await client.post(HOST + "/documents/", data=form)
            assert response.status_code == status.HTTP_200_OK

    async def test_create_document_with_error(self):
        async with httpx.AsyncClient() as client:
            form = {"text": SAMPLE_SHORT_TEXT}
            response = await client.post(HOST + "/documents/", data=form)
            assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    async def test_get_existing_document_summary(self):
        async with httpx.AsyncClient() as client:
            form = {"text": SAMPLE_LARGE_TEXT}
            r = await client.post(HOST + "/documents/", data=form)
            document_id = r.json()['document_id']
            response = await client.get(HOST + "/documents/{}/summary/".format(document_id))
            assert response.status_code == status.HTTP_200_OK

    async def test_get_non_existing_document_summary(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(HOST + "/documents/0/summary/")
            assert response.status_code == status.HTTP_404_NOT_FOUND
