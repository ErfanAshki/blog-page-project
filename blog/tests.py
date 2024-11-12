from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='erf', email='erf@gmail.com', password='erf123')
        cls.post = Post.objects.create(
            title='title1',
            description='des1',
            author=cls.user
        )
        cls.post2 = Post.objects.create(
            title='title2',
            description='des2',
            author=cls.user,
            status=Post.STATUS_CONDITION[1][0]
        )

    def test_just_only_show_published_post(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post.title)
        self.assertNotContains(response, self.post2.title)

    def test_list_view(self):
        response = self.client.get('/post/list/')
        self.assertEqual(response.status_code, 200)

    def test_list_view_with_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_title_in_list_view(self):
        response = self.client.get('/post/list/')
        self.assertContains(response, self.post.title)

    def test_title_in_list_view_with_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post.title)

    def test_title_in_detail_view(self):
        response = self.client.get(f'/post/{self.post.id}/')
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.description)

    def test_title_in_detail_view_with_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.description)

    def test_detail_view(self):
        response = self.client.get(f'/post/{self.post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_with_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_out_of_range_blog(self):
        response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code, 404)

    def test_out_of_range_blog_with_name(self):
        response = self.client.get(reverse('post_detail', args=[8552]))
        self.assertEqual(response.status_code, 404)

    def test_is_inheritance_from_template_in_list_view(self):
        response = self.client.get('/post/list/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_is_inheritance_from_template_in_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_title_in_page_equal_to_title_in_database(self):
        self.assertEqual(self.post.title, 'title1')
        self.assertEqual(self.post2.title, 'title2')
        self.assertEqual(self.post.description, 'des1')
        self.assertEqual(self.post2.description, 'des2')

    def test_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'some title',
            'description': 'some description',
            'author': self.user.id,
            'status': 'PUB',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some title')
        self.assertEqual(Post.objects.last().description, 'some description')

    def test_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'updated title',
            'description': 'updated description',
            'author': self.post2.author.id,
            'status': 'PUB',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'updated title')
        self.assertEqual(Post.objects.last().description, 'updated description')

    def test_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)

