import json
import urllib.request

def lambda_handler(event, context):
    # Get the URL from the request body
    body = json.loads(event.get('body', '{}'))
    url = body.get('url', '')

    if not url:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Please provide a url in the request body'})
        }

    try:
        # Open the URL and read headers (doesn't download the full file)
        req = urllib.request.urlopen(url, timeout=5)
        size_bytes = req.headers.get('Content-Length', 'unknown')
        content_type = req.headers.get('Content-Type', 'unknown')

        return {
            'statusCode': 200,
            'body': json.dumps({
                'url': url,
                'content_type': content_type,
                'size_bytes': size_bytes,
                'message': 'Successfully fetched file info!'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }